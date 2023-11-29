
# 2023-11-21_arrow-over-http-scratchpad

Experiments related to the Arrow over HTTP discussion at https://lists.apache.org/thread/vfz74gv1knnhjdkro47shzd1z5g5ggnf

Requires `pip install flask pyarrow`.

Run the Flask app:

```shell
python app.py
#> * Running on http://127.0.0.1:5000
#> Press CTRL+C to quit
```

Perform an HTTP request:

```shell
python client.py http://127.0.0.1:5000 get_ipc
#> Response batch 0:
#> pyarrow.RecordBatch
#> int: int64
#> string: string
#> ----
#> int: [0,1,2,3,4,5,6,7,8,9,...,16,17,18,19,20,21,22,23,24,25]
#> string: ["a","b","c","d","e","f","g","h","i","j",...,"q","r","s","t","u","v","w","x","y","z"]
```
