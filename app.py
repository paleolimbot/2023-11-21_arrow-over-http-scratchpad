import io
from flask import Flask, request
import pyarrow as pa
import pyarrow.ipc as ipc


app = Flask(__name__)


# Dummy dataset for now
def make_reader():
    data = pa.table([range(26), "abcdefghijklmnopqrstuvwxyz"], ["int", "string"])
    return pa.RecordBatchReader.from_batches(data.schema, data.to_batches())


# iterator of bytes (how Flask streams output)
def make_result_generator(reader, options):
    with io.BytesIO() as f, ipc.new_stream(f, reader.schema, options=options) as stream:
        yield f.getvalue()

        for batch in reader:
            f.seek(0)
            f.truncate(0)
            stream.write_batch(batch)
            yield f.getvalue()

        f.seek(0)
        f.truncate(0)
        stream.close()
        yield f.getvalue()


@app.route("/get_ipc")
def get_ipc():
    compression = request.args.get("compression", None)
    compression_level = request.args.get("compression_level", None)
    if compression is not None and compression_level is not None:
        compression = pa.Codec(compression, int(compression_level))

    options = ipc.IpcWriteOptions(compression=compression)

    result = make_result_generator(make_reader(), options)

    return app.response_class(
        result,
        mimetype="application/vnd.apache.arrow.stream",
    )


if __name__ == "__main__":
    app.run(debug=True, port=5000)
