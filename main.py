meme_dict = {
            "CRINGE": "Sesuatu yang sangat aneh atau memalukan",
            "LOL": "Tanggapan umum terhadap sesuatu yang lucu",
            }
            
word = input("Ketik kata yang tidak Kamu mengerti (gunakan huruf kapital semua!): ")            
            
if word in meme_dict.keys():
    print('makna dari',word,'adaalah',meme_dict[word])
else:
    print('kata itu tidak di temukan')       
