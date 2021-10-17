import input.bu_bu_gao
import input.nao_bai_jin
import input.the_elder

import model.cpm2


sentence = input.bu_bu_gao.input_text

model.cpm2.generate(sentence)
