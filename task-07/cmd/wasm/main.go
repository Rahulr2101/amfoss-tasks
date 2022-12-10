package main

import (
	"syscall/js"
)

var Count = 0

func add(this js.Value, i []js.Value) interface{} {
	Count += 1
	document := js.Global().Get("document")
	p := document.Call("getElementById", "int")
	p.Set("innerText", Count)
	return Count
}

func sub(this js.Value, i []js.Value) interface{} {
	Count -= 1
	document := js.Global().Get("document")
	p := document.Call("getElementById", "int")
	p.Set("innerHTML", Count)

	return Count
}

func reset(this js.Value, i []js.Value) interface{} {
	Count = 0
	document := js.Global().Get("document")
	p := document.Call("getElementById", "int")
	p.Set("innerHTML", Count)

	return Count
}

func registerCallbacks() {
	js.Global().Set("add", js.FuncOf(add))
	js.Global().Set("sub", js.FuncOf(sub))
	js.Global().Set("reset", js.FuncOf(reset))
}
func main() {
	c := make(chan struct{}, 0)
	println("Hello world")
	registerCallbacks()
	<-c
}
