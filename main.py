from datetime import datetime
from scraper.browser import create_browser
from scraper.utility import merge_fields, preprocess
from scraper.parser import get_field_names, get_rows, parse_row,set_no_of_rows
from scraper.navigation import go_to_next_page
from scraper.writer import write_header, write_row

driver = create_browser(headless=True)
driver.set_page_load_timeout(120)
driver.get("https://finance.yahoo.com/markets/stocks/most-active/?start=0&count=100")
set_no_of_rows(driver)
try:
    fields = get_field_names(driver)
    merge_fields(fields, "P/E Ratio", "(TTM)", "P/E Ratio (TTM)")
    merge_fields(fields, "52 Wk", "Change %", "52 Wk Change %")
    field_names = preprocess(fields)

    filename = f"stock_data_{datetime.now().strftime('%d-%m-%y_%I-%M-%S_%p')}.csv"
    with open(filename, "w", newline="\n", encoding="UTF-8") as csvfile:
        import csv
        writer = csv.writer(csvfile)
        write_header(writer, field_names)

        while True:
            rows = get_rows(driver)
            prev_first_row = rows[0].text
            for row in rows:
                parsed = parse_row(row)
                write_row(writer, parsed)
            if not go_to_next_page(driver, prev_first_row):
                print("End of pages")
                break
finally:
    driver.quit()
