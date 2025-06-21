from arguments.args import aggregate, order_by, where, name
from core.aggregate import file_aggregate_print
from core.filter import file_filter_print, filter_file
from core.order import file_order_by_print
from core.read import file_print, reader_file


def main():
    data = reader_file(name)
    if where and aggregate:
        filtered_data = filter_file(data, where)
        filtered_data_with_header = [data[0]] + filtered_data
        file_aggregate_print(filtered_data_with_header, aggregate)
    elif where and order_by:
        filtered = filter_file(data, where)
        filtered_with_header = [data[0]] + filtered
        file_order_by_print(filtered_with_header, order_by)
    elif where:
        file_filter_print(data, where)
    elif aggregate:
        file_aggregate_print(data, aggregate)
    elif order_by:
        file_order_by_print(data, order_by)
    else:
        file_print(data)


if __name__ == "__main__":
    main()
