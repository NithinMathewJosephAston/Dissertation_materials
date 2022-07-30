import spacy
import random
import json
from spacy.training.example import Example


def train_spacy(dataset, iterations):
    nlp = spacy.blank('en')  # create blank Language class
    # create the built-in pipeline components and add them to the pipeline
    # nlp.create_pipe works for built-ins that are registered with spaCy
    ner = ''
    if 'ner' not in nlp.pipe_names:
        ner = nlp.add_pipe('ner', last=True)

    # add labels
    for annotations in dataset["annotations"]:
        for ent in annotations[-1]['entities']:
            ner.add_label(ent[-1])

    # get names of other pipes to disable them during training
    other_pipes = [pipe for pipe in nlp.pipe_names if pipe != 'ner']
    with nlp.disable_pipes(*other_pipes):  # only train NER
        optimizer = nlp.begin_training()
        for itn in range(iterations):
            print("Starting iteration " + str(itn))
            # random.shuffle(dataset)
            losses = {}
            for annotations in dataset["annotations"]:
                doc = nlp.make_doc(annotations[0])
                example = Example.from_dict(doc, annotations[-1])
                nlp.update(
                    [example],
                    drop=0.2,  # dropout - make it harder to memorise data
                    sgd=optimizer,  # callable to update weights
                    losses=losses)
            print(losses)
    return nlp


if __name__=='__main__':
    with open("annotations.json", 'r') as dataset:
        json_dataset = dataset.read()
    json_file = json.loads(json_dataset)
    legal_model = train_spacy(json_file, 20)

    # Save trained Model
    model_file = input("Enter your Model Name: ")
    legal_model.to_disk(model_file)

    with open("data_crunching_1.txt", 'r') as test_dataset:
        test_text = test_dataset.read()
    doc = legal_model(test_text)
    for ent in doc.ents:
        print(ent.text, ent.start_char, ent.end_char, ent.label_)
    pass
