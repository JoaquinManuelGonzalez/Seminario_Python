evaluar = """ título: Experiences in Developing a Distributed Agent-based 
Modeling Toolkit with Python
resumen: Distributed agent-based modeling (ABM) on high-performance 
computing resources provides the promise of capturing unprecedented details 
of large-scale complex systems. However, the specialized knowledge required 
for developing such ABMs creates barriers to wider adoption and utilization. 
Here we present our experiences in developing an initial implementation of 
Repast4Py, a Python-based distributed ABM toolkit. We build on our 
experiences in developing ABM toolkits, including Repast for High 
Performance Computing (Repast HPC), to identify the key elements of a useful 
distributed ABM toolkit. We leverage the Numba, NumPy, and PyTorch packages 
and the Python C-API to create a scalable modeling system that can exploit 
the largest HPC resources and emerging computing architectures.
"""
#Resumo y proceso al titulo
tittle = evaluar.split("resumen: ")[0].split("título: ")[1].split("\n")[0]
tittle = tittle.split(" ")
tittle_two = evaluar.split("resumen: ")[0].split("título: ")[1].split("\n")[1]
tittle_two = tittle_two.split(" ")
tittle.extend(tittle_two)
tittle.remove("")
if len(tittle) <= 10:
    print("El titulo cumple las condiciones especificadas")
else:
    print("El titulo no cumple con las condiciones especificadas")

#Resumo y proceso al resumen
easy = acceptable = hard = very_hard = 0
summary = evaluar.split("resumen: ")[1]
sentences = summary.split(".")
sentences.remove("\n")
for elem in sentences:
    words = elem.split(" ")
    if "" in words:
        words.remove("")
    cant_words = len(words)
    match cant_words:
        case cant_words if cant_words < 12:
            easy += 1
        case cant_words if 12 <= cant_words <= 17:
            acceptable += 1
        case cant_words if 18 <= cant_words <= 25:
            hard += 1
        case cant_words if cant_words > 25:
            very_hard += 1
print(f"El texto tiene {easy} oraciones faciles de leer")  
print(f"El texto tiene {acceptable} oraciones aceptables de leer")  
print(f"El texto tiene {hard} oraciones dificiles de leer")  
print(f"El texto tiene {very_hard} oraciones muy dificiles de leer")  