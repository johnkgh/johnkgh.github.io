---
layout: post
title: "Implementing a State Machine"
tags: [Python]
---

Implementing a State Machine

Brainfuck, meanwhile, takes assembly instructions and reduces them to the barest
whisps of code, which more or less approximates a Turing machine.


Character	Meaning
>	increment the data pointer (to point to the next cell to the right).
<	decrement the data pointer (to point to the next cell to the left).
+	increment (increase by one) the byte at the data pointer.
-	decrement (decrease by one) the byte at the data pointer.
.	output the byte at the data pointer.
,	accept one byte of input, storing its value in the byte at the data pointer.
[	if the byte at the data pointer is zero, then instead of moving the instruction pointer forward to the next command, jump it forward to the command after the matching ] command.
]	if the byte at the data pointer is nonzero, then instead of moving the instruction pointer forward to the next command, jump it back to the command after the matching [ command.


<!--more-->

```python

```
