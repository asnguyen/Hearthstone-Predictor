import itertools

def create_ngrams_from_file(n, card_played):
    list_ngram = []
    for x in range(len(card_played) - int(n)):
        ngram = []
        for y in range(int(n)):
            ngram.append(card_played[x+y])
        list_ngram.append(tuple(ngram))
    return list_ngram

def update_dataset(trigrams, dataset):
    #dataset = dict()
    for i in trigrams:
        if i not in dataset:
            dataset[i] = 0
        dataset[i] += 1
        comb = list(itertools.combinations(list(i),2))
        for j in comb:
            if j not in dataset:
                dataset[j]=0
            dataset[j]+=1
    #return dataset

def read_in_data(fileText):
    file_object = open(fileText,"r")
    card_played = dict()
    i = 0
    for line in file_object:
        card_played[i] = line.replace("\n","")
        i+=1
    list_ngram = create_ngrams_from_file(3,card_played)

    return list_ngram

def print_tuple(tup):
    val = "( "
    lst = list(tup)
    for i in lst:
        val = val + str(i) + " "
    val = val + ")"
    return val

def main():
    print("Begin Code")

    filename = "sample_text1.txt"
    list_ngram = read_in_data(filename)

    dataset = dict()

    update_dataset(list_ngram, dataset)

    print(len(dataset.keys()))

    for key in dataset.keys():
        print(str(key)+" : "+str(dataset[key]))

    print("End Code")

if __name__ == "__main__":
    main()