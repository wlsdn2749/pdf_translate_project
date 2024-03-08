# PDF Translation ( English -> Korean Only)

This repository is created for study time efficiency. Generally, Normal Korean (like me) has struggle to read original english book or papers. As a sneak peek of reading original book, If you read translated book once reading original book, This program maybe helpful to understand original book.

---

### Folder Structures

1. __nllb__

    nllb is open-source machine translation model by [huggingface](https://huggingface.co/NHNDQ/nllb-finetuned-en2ko). specially use korean finetuned model by [NHNDQ](https://huggingface.co/NHNDQ). In this project, nllb fully takes part of translation english into korean. 


2. __pdf_translate__

- First, Reading PDF in locals. 
- Second, Transform PDF into DOCX.
- Third, Read by line, POST request to nllb (To localhost:8000/translated)
- Finally, Write new docx based in korean translated.



---
### Results

[Source](https://www.gameaipro.com/)

#### Original PDF
![image](https://github.com/wlsdn2749/Lightning-CoreRL/assets/91457439/df3aca66-c515-4b20-9417-8a5e8e3f8412){: width="400" height="400"}


#### Transformed Docx
![image](https://github.com/wlsdn2749/Lightning-CoreRL/assets/91457439/cb5f9c3b-777a-40bd-acd6-035ea3fe9400){: width="400" height="400"}|

#### Tnanslated Docx

![image](https://github.com/wlsdn2749/Lightning-CoreRL/assets/91457439/7c82c30c-d2f6-40e2-b0cf-7e0b41e6f8a1){: width="500" height="600"}|



---
### To-do
- Align Original PDF Structures
- Write Non-text elements (Pictures ...)


---
### Aim to make like this
![image](https://github.com/wlsdn2749/Lightning-CoreRL/assets/91457439/dbe9a5eb-d65c-40f0-af4f-f72bc7b6167c){: width="500" height="600"}|








