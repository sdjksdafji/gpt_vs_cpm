import bminf
import sys

cpm2_1 = bminf.models.CPM2()


def generate(text, min_iter=5, max_iter=10):
    model = cpm2_1
    print("Input: ", text)
    sys.stdout.write("Output: %s" % text)
    stoped = False
    iter = 0
    while (iter < min_iter or not stoped) and (not iter > max_iter):
        value, stoped = model.generate(
            input_sentence=text,
            max_tokens=32,
            top_n=5,
            top_p=None,
            temperature=0.95,
            frequency_penalty=0,
            presence_penalty=1,
        )
        text += value
        iter += 1
        sys.stdout.write(value)
        sys.stdout.flush()
    sys.stdout.write("\n")
