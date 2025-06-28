def merge_fields(field_names, first, second, combined):
    if first in field_names:
        i = field_names.index(first)
        if i + 1 < len(field_names) and field_names[i + 1] == second:
            field_names[i] = combined
            del field_names[i + 1]

def preprocess(field_names):
    field_names = [field.strip() for field in field_names]
    for unwanted in ["52 Wk Range"]:
        if unwanted in field_names:
            field_names.remove(unwanted)
    return field_names
