from hypothesisfuzzer import FuzzServer

fuzzer = FuzzServer()
fuzzer.run(host='0.0.0.0', port=80)
