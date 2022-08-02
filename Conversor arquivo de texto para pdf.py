#pip install aspose-words(para instalar a biblioteca necessária)
import aspose.words as aw

#Documento utilizado para conversão
doc = aw.Document("nomedodocumento.docx")

#PDF de saída
doc.save("nomedodocumento.pdf")