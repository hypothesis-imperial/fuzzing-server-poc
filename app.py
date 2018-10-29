from hypothesisfuzzer import Fuzzer

fuzzer = Fuzzer('config.yml')
fuzzer.run(host='0.0.0.0', port=80)
