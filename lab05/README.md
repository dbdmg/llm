## Lab 05

The fift lab is divided into two parts:
- quantization: in this part we see how quantization works, by first implementing absmax (symmetric) and minmax (asymmetric) quantizations; and then using dynamic quantization to quantize a model (post-training).

- LoRA: this part focuses on applying LoRA to a BERT model, with the goal of fine-tuning it (but changing fewer parameters). We first implement LoRA ourselves. Next, we use th HF PEFT library to apply LoRA directly. 

The following are the files you will use for this lab:
- quantization exercise ([text](./text-01-quantization.ipynb)) ([solution](./solution-01-quantization.ipynb))
- LoRA exercise ([text](./text-02-LoRA.ipynb)) ([solution](./solution-02-LoRA.ipynb))
