import extism

path ="zig-out/bin/zig-pdk-template.wasm"
wasm = open(path, 'rb').read()
manifest = {"wasm": [{"data": wasm}]}
plugin=extism.Plugin(manifest)
out = plugin.call("greet", "YOLO")
print(out)