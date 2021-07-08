

output = "Shivaji Bhonsale February 1630, 3 April 1680, also referred to as Chhatrapati Shivaji, was an Indian ruler and a member of the Bhonsle Maratha clan. Shivaji carved out an enclave from the declining Adilshahi sultanate of Bijapur that formed the genesis of the Maratha Empire. In 1674, he was formally crowned the Chhatrapati (emperor) of his realm at Raigad. Over the course of his life, Shivaji engaged in both alliances and hostilities with the Mughal Empire, the Sultanate of Golkonda and the Sultanate of Bijapur, as well as with European colonial powers. Shivaji's military forces expanded the Maratha sphere of influence, capturing and building forts, and forming a Maratha navy. Shivaji established a competent and progressive civil rule with well-structured administrative organisations. He revived ancient Hindu political traditions and court conventions and promoted the usage of the Marathi language. Shivaji's legacy was to vary by observer and time, but nearly two centuries after his death, he began to take on increased importance with the emergence of the Indian independence movement, as many Indian nationalists elevated him as a proto-nationalist and hero of the Hindus."

def summary(output):
    import requests
    
    url = "https://textanalysis-text-summarization.p.rapidapi.com/text-summarizer-text"
    
    payload = "text=" +output+ "&sentnum=5"
    #print(payload)
    headers = {
        'content-type': "application/x-www-form-urlencoded",
        'x-rapidapi-key': "b03ee82bbcmsh3579e3fca7285e5p1ce1a4jsnc7bb6182f40c",
        'x-rapidapi-host': "textanalysis-text-summarization.p.rapidapi.com"
        }
    
    response = requests.request("POST", url, data=payload, headers=headers)
    #print('----')
    print(response.text)
    
    
summary(output)