import one_get_api as oga
import two_mapping_to_identifier as tmti
import three_word2vec as tw
import four_deep_learning as fdl
import time
from reader import read_constant, read_dict
from tools import folders_set

if __name__ == "__main__":
    folders_set()
    globals = read_constant()  # 读取json数据
    with open(globals['log_path'], 'a+') as fp:
        start = time.time()
        oga.get_api(globals['TYPE_list'],globals['apk_path'],globals['apis_path'])
        fp.write('one step : '+str(time.time() - start))
        fp.write('\n')


        dic = read_dict(globals['mapping_to_identifier_path'])
        start = time.time()
        tmti.process_mapping_to_identifier(globals['TYPE'],globals['TYPE_list'],dic,globals['apis_path'],globals['train_path'],globals['test_path'],globals['val_split'])
        fp.write('second step : '+str(time.time() - start))
        fp.write('\n')


        start = time.time()
        model = tw.word2vec_model(globals['TYPE'], globals['TYPE_list'],globals['train_path'],globals['test_path'],globals['word2vec_model_path'],globals['K'])
        fp.write('third step : '+str(time.time() - start))
        fp.write('\n')


        start = time.time()
        fdl.deep_learning(globals['TYPE'], globals['TYPE_list'], globals['type_map'], model,globals)
        fp.write('fourth step: '+str(time.time() - start))
        fp.write('\n')
        fp.close()
