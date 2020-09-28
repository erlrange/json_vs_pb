import argparse
import time

BENCH_MODE_JSON = 'json'
BENCH_MODE_PROTOBUF = 'protobuf'
BENCH_MODE_SIMPLE_JSON = 'simplejson'

parser = argparse.ArgumentParser(description="Some serialization benchmark for fun: json vs protobuf")
parser.add_argument("mode", choices=[BENCH_MODE_JSON, BENCH_MODE_PROTOBUF, BENCH_MODE_SIMPLE_JSON])
parser.add_argument("--iterations", dest="iterations", default=10000, type=int)

args = parser.parse_args()

if args.mode == BENCH_MODE_PROTOBUF:
    from runners.protobuf import run
elif args.mode == BENCH_MODE_JSON:
    from runners.json import run
elif args.mode == BENCH_MODE_SIMPLE_JSON:
    from runners.simplejson import run

start_time = time.time()
for _ in range(args.iterations):
    run()
end_time = time.time()

print('>> Result: ', end_time - start_time)
