from struct import Struct


def write_records(records, format, f):
    record_struct = Struct(format)
    for r in records:
        f.write(record_struct.pack(*r))


def unpack_records(format, data):
    record_struct = Struct(format)
    return (record_struct.unpack_from(data, offset) for offset in range(0, len(data), record_struct.size))


if __name__ == '__main__':
    records = [(1, 2.3, 4.5),
               (6, 7.8, 9.0),
               (12, 13.4, 56.7)]

    with open('data.b', 'wb') as f:
        write_records(records, '<idd', f)

    from collections import namedtuple

    Record = namedtuple('Record', ['kind', 'x', 'y'])

    with open('data.b', 'rb') as f:
        data = f.read()

        for rec in unpack_records('<idd', data):
             record = Record(*rec)
             print record