"""
プレイヤー　　　　       プレイヤー１、プレイヤー２
プレイヤー１　 　      　好きな単語を選んで隠しておく
                    　単語の文字数だけアンダーバーを引く
                    　プレイヤー２が回答した文字が隠してある単語に含まれていたら、書いておいたアンダーバーのその文字があるbrきところにその文字を表示
                    　ひとつの単語に同じ文字が２個以上含まれている場合は回答１回につき１文字だけ表示
                    　プレイヤー２の回答が間違っていたら吊られた人の絵のパーツをひとつ書き込む（頭から始める）
プレイヤー２            単語を予想して１回に１文字を回答する
勝敗　　               吊られた絵が完成する前に隠された文字を全て当てられたらプレイヤー２の勝ち
                    　絵が完成したらプレイヤー２の負け

"""

def hangman(word):
    wrong = 0
    stages = ["",
              "__________          ",
              "|         |",
              "|         |         ",
              "|         O         ",
              "|        /|\        ",
              "|        / \        ",
              "|                   "
              ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("ハングマンへようこそ！")


    while wrong < len(stages)-1:
        print("\n")
        msg = "１文字を予想してね    "
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = "$"
        else :
            wrong += 1
        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("あなたの勝ち！")
            print("_".join(board))
            win = True
            break
    if not win :
        print("\n".join(stages[0:wrong+1]))
        print("あなたの負け！正解は　{}.")

hangman("cat")
