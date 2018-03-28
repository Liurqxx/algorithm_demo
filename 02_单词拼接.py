# _*_ coding:utf-8 _*_
# Author:liu
'''
    单词拼接:
        给一些单词，判断能否把它们首尾串起来串成一串。
        前一个单词的结尾应该与下一个单词的首字母相同。
'''


# aloha
# dog
# arachnid
# gopher
# tiger
# rat
# 拼接后：aloha.arachnid.dog.gopher.rat.tiger

def main():
    # word_list = []
    # num = int(input("请输入单词的个数:"))
    # for i in range(num):
    #     word_str = input("请输入第%d个单词:" % (i + 1))
    #     word_list.append(word_str)

    word_list = ['aloha', 'dog', 'arachnid', 'gopher', 'tiger', 'rat']
    old_len = len(word_list)
    front_world = word_list[0]
    result_word = []
    while True:
        for word in word_list:
            if word[0] == front_world[0]:
                if word[-1:-2:-1] < front_world[-1:-2:-1]:
                    front_world = word

            if word[0] == front_world[-1:-2:-1]:
                result_word.append(word)
                word_list.remove(word)
                front_world = word
                # print(result_word)
        if len(result_word) == old_len and not len(word_list):
            print(result_word)
            break


if __name__ == '__main__':
    main()
