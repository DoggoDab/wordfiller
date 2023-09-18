import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox

def start_screen(adventure_button, go_back_button, canvas, scroll_bar, frame, go_back_button_2, generate_level_one_button, go_back_button_level_one, label_story, level_one_frame, level_two_generate_button, level_two_go_back_button, label_story_level_two, level_two_frame, level_three_generate_button, level_three_go_back_button, level_three_label_story, level_three_menu_adjective_button, level_three_menu_adjective2_button, level_three_menu_noun_button, level_three_menu_noun2_button, level_three_menu_verb_button, level_three_frame, level_four_generate_button, level_four_go_back_button, level_four_story_label, level_four_menu_adjective_button, level_four_menu_noun_button, level_four_menu_verb_button, level_four_menu_noun2_button, level_four_menu_noun3_button, level_four_frame, level_five_generate_button, level_five_go_back_button, level_five_story_label, level_five_frame, level_five_menu_adjective_button, level_five_menu_noun_button, level_five_menu_adverb_button, level_five_menu_verb_button, level_six_go_back_button, level_six_generate_button, level_six_story_label, level_six_frame, level_six_menu_adjective_button, level_six_menu_noun_button, level_six_menu_verb_button, level_six_menu_adjective2_button, level_six_menu_noun2_button, level_six_menu_noun3_button, level_seven_menu_adjective_button, level_seven_menu_noun_button, level_seven_menu_adjective2_button, level_seven_menu_verb_button, level_seven_menu_adjective3_button, level_seven_menu_noun2_button, level_seven_go_back_button, level_seven_generate_button, level_seven_story_label, level_seven_frame, level_eight_go_back_button, level_eight_generate_button, level_eight_story_label, level_eight_frame, level_eight_menu_noun_button, level_eight_menu_adjective_button, level_eight_menu_noun2_button, level_eight_menu_verb_button, level_eight_menu_noun3_button, level_eight_menu_verb2_button, level_eight_menu_adjective2_button, level_eight_menu_noun4_button, level_nine_go_back_button, level_nine_generate_button, level_nine_story_label, level_nine_frame, level_nine_menu_adjective_button, level_nine_menu_noun_button, level_nine_menu_verb_button, level_nine_menu_verb2_button, level_nine_menu_noun2_button, level_ten_go_back_button, level_ten_generate_button, level_ten_story_label, level_ten_frame, level_ten_menu_noun_button, level_ten_menu_verb_button, level_ten_menu_verb2_button, level_ten_menu_verb3_button, level_ten_menu_noun2_button): 
    l = tk.Label(root, text="Welcome to WordFiller".upper(), font=("Bauhaus 93", 24), background='#35393e', fg='#CAF1DE')
    start_button = tk.Button(root, text="Play".upper(), width=40, height=10, background='#5D6064', command=lambda: start_game(l, start_button, canvas, scroll_bar, frame, go_back_button_2, generate_level_one_button, go_back_button_level_one, label_story, level_one_frame, level_two_generate_button, level_two_go_back_button, label_story_level_two, level_two_frame, level_three_generate_button, level_three_go_back_button, level_three_label_story, level_three_menu_adjective_button, level_three_menu_adjective2_button, level_three_menu_noun_button, level_three_menu_noun2_button, level_three_menu_verb_button, level_three_frame, level_four_generate_button, level_four_go_back_button, level_four_story_label, level_four_menu_adjective_button, level_four_menu_noun_button, level_four_menu_verb_button, level_four_menu_noun2_button, level_four_menu_noun3_button, level_four_frame, level_five_generate_button, level_five_go_back_button, level_five_story_label, level_five_frame, level_five_menu_adjective_button, level_five_menu_noun_button, level_five_menu_adverb_button, level_five_menu_verb_button, level_six_go_back_button, level_six_generate_button, level_six_story_label, level_six_frame, level_six_menu_adjective_button, level_six_menu_noun_button, level_six_menu_verb_button, level_six_menu_adjective2_button, level_six_menu_noun2_button, level_six_menu_noun3_button, level_seven_menu_adjective_button, level_seven_menu_noun_button, level_seven_menu_adjective2_button, level_seven_menu_verb_button, level_seven_menu_adjective3_button, level_seven_menu_noun2_button, level_seven_go_back_button, level_seven_generate_button, level_seven_story_label, level_seven_frame, level_eight_go_back_button, level_eight_generate_button, level_eight_story_label, level_eight_frame, level_eight_menu_noun_button, level_eight_menu_adjective_button, level_eight_menu_noun2_button, level_eight_menu_verb_button, level_eight_menu_noun3_button, level_eight_menu_verb2_button, level_eight_menu_adjective2_button, level_eight_menu_noun4_button, level_nine_go_back_button, level_nine_generate_button, level_nine_story_label, level_nine_frame, level_nine_menu_adjective_button, level_nine_menu_noun_button, level_nine_menu_verb_button, level_nine_menu_verb2_button, level_nine_menu_noun2_button, level_ten_go_back_button, level_ten_generate_button, level_ten_story_label, level_ten_frame, level_ten_menu_noun_button, level_ten_menu_verb_button, level_ten_menu_verb2_button, level_ten_menu_verb3_button, level_ten_menu_noun2_button))

    l.pack(side='top', pady=40)
    start_button.pack(side='top', padx=50)

    adventure_button.pack_forget()
    go_back_button.pack_forget()

def start_game(l, start_button, canvas, scroll_bar, frame, go_back_button_2, generate_level_one_button, go_back_button_level_one, label_story, level_one_frame, level_two_generate_button, level_two_go_back_button, label_story_level_two, level_two_frame, level_three_generate_button, level_three_go_back_button, level_three_label_story, level_three_menu_adjective_button, level_three_menu_adjective2_button, level_three_menu_noun_button, level_three_menu_noun2_button, level_three_menu_verb_button, level_three_frame, level_four_generate_button, level_four_go_back_button, level_four_story_label, level_four_menu_adjective_button, level_four_menu_noun_button, level_four_menu_verb_button, level_four_menu_noun2_button, level_four_menu_noun3_button, level_four_frame, level_five_generate_button, level_five_go_back_button, level_five_story_label, level_five_frame, level_five_menu_adjective_button, level_five_menu_noun_button, level_five_menu_adverb_button, level_five_menu_verb_button, level_six_go_back_button, level_six_generate_button, level_six_story_label, level_six_frame, level_six_menu_adjective_button, level_six_menu_noun_button, level_six_menu_verb_button, level_six_menu_adjective2_button, level_six_menu_noun2_button, level_six_menu_noun3_button, level_seven_menu_adjective_button, level_seven_menu_noun_button, level_seven_menu_adjective2_button, level_seven_menu_verb_button, level_seven_menu_adjective3_button, level_seven_menu_noun2_button, level_seven_go_back_button, level_seven_generate_button, level_seven_story_label, level_seven_frame, level_eight_go_back_button, level_eight_generate_button, level_eight_story_label, level_eight_frame, level_eight_menu_noun_button, level_eight_menu_adjective_button, level_eight_menu_noun2_button, level_eight_menu_verb_button, level_eight_menu_noun3_button, level_eight_menu_verb2_button, level_eight_menu_adjective2_button, level_eight_menu_noun4_button, level_nine_go_back_button, level_nine_generate_button, level_nine_story_label, level_nine_frame, level_nine_menu_adjective_button, level_nine_menu_noun_button, level_nine_menu_verb_button, level_nine_menu_verb2_button, level_nine_menu_noun2_button, level_ten_go_back_button, level_ten_generate_button, level_ten_story_label, level_ten_frame, level_ten_menu_noun_button, level_ten_menu_verb_button, level_ten_menu_verb2_button, level_ten_menu_verb3_button, level_ten_menu_noun2_button): 

    adventure_button = tk.Button(root, text="adventure".upper(), width=20, height=5, background='#5D6064', command=lambda: adventure_game(adventure_button, go_back_button, l, start_button, generate_level_one_button, go_back_button_level_one, label_story, level_one_frame, level_two_generate_button, level_two_go_back_button, label_story_level_two, level_two_frame, level_three_generate_button, level_three_go_back_button, level_three_label_story, level_three_menu_adjective_button, level_three_menu_adjective2_button, level_three_menu_noun_button, level_three_menu_noun2_button, level_three_menu_verb_button, level_three_frame, level_four_generate_button, level_four_go_back_button, level_four_story_label, level_four_menu_adjective_button, level_four_menu_noun_button, level_four_menu_verb_button, level_four_menu_noun2_button, level_four_menu_noun3_button, level_four_frame, level_five_generate_button, level_five_go_back_button, level_five_story_label, level_five_frame, level_five_menu_adjective_button, level_five_menu_noun_button, level_five_menu_adverb_button, level_five_menu_verb_button, level_six_go_back_button, level_six_generate_button, level_six_story_label, level_six_frame, level_six_menu_adjective_button, level_six_menu_noun_button, level_six_menu_verb_button, level_six_menu_adjective2_button, level_six_menu_noun2_button, level_six_menu_noun3_button, level_seven_go_back_button, level_seven_generate_button, level_seven_story_label, level_seven_frame, level_seven_menu_adjective_button, level_seven_menu_noun_button, level_seven_menu_adjective2_button, level_seven_menu_verb_button, level_seven_menu_adjective3_button, level_seven_menu_noun2_button, level_eight_go_back_button, level_eight_generate_button, level_eight_story_label, level_eight_frame, level_eight_menu_noun_button, level_eight_menu_adjective_button, level_eight_menu_noun2_button, level_eight_menu_verb_button, level_eight_menu_noun3_button, level_eight_menu_verb2_button, level_eight_menu_adjective2_button, level_eight_menu_noun4_button, level_nine_go_back_button, level_nine_generate_button, level_nine_story_label, level_nine_frame, level_nine_menu_adjective_button, level_nine_menu_noun_button, level_nine_menu_verb_button, level_nine_menu_verb2_button, level_nine_menu_noun2_button, level_ten_go_back_button, level_ten_generate_button, level_ten_story_label, level_ten_frame, level_ten_menu_noun_button, level_ten_menu_verb_button, level_ten_menu_verb2_button, level_ten_menu_verb3_button, level_ten_menu_noun2_button))
    go_back_button = tk.Button(root, text="go back".upper(), width=20, height=5, background='#5D6064', command=lambda: start_screen(adventure_button, go_back_button, canvas, scroll_bar, frame, go_back_button_2, generate_level_one_button, go_back_button_level_one, label_story, level_one_frame, level_two_generate_button, level_two_go_back_button, label_story_level_two, level_two_frame, level_three_generate_button, level_three_go_back_button, level_three_label_story, level_three_menu_adjective_button, level_three_menu_adjective2_button, level_three_menu_noun_button, level_three_menu_noun2_button, level_three_menu_verb_button, level_three_frame, level_four_generate_button, level_four_go_back_button, level_four_story_label, level_four_menu_adjective_button, level_four_menu_noun_button, level_four_menu_verb_button, level_four_menu_noun2_button, level_four_menu_noun3_button, level_four_frame, level_five_generate_button, level_five_go_back_button, level_five_story_label, level_five_frame, level_five_menu_adjective_button, level_five_menu_noun_button, level_five_menu_adverb_button, level_five_menu_verb_button, level_six_go_back_button, level_six_generate_button, level_six_story_label, level_six_frame, level_six_menu_adjective_button, level_six_menu_noun_button, level_six_menu_verb_button, level_six_menu_adjective2_button, level_six_menu_noun2_button, level_six_menu_noun3_button, level_seven_menu_adjective_button, level_seven_menu_noun_button, level_seven_menu_adjective2_button, level_seven_menu_verb_button, level_seven_menu_adjective3_button, level_seven_menu_noun2_button, level_seven_go_back_button, level_seven_generate_button, level_seven_story_label, level_seven_frame, level_eight_go_back_button, level_eight_generate_button, level_eight_story_label, level_eight_frame, level_eight_menu_noun_button, level_eight_menu_adjective_button, level_eight_menu_noun2_button, level_eight_menu_verb_button, level_eight_menu_noun3_button, level_eight_menu_verb2_button, level_eight_menu_adjective2_button, level_eight_menu_noun4_button, level_nine_go_back_button, level_nine_generate_button, level_nine_story_label, level_nine_frame, level_nine_menu_adjective_button, level_nine_menu_noun_button, level_nine_menu_verb_button, level_nine_menu_verb2_button, level_nine_menu_noun2_button, level_ten_go_back_button, level_ten_generate_button, level_ten_story_label, level_ten_frame, level_ten_menu_noun_button, level_ten_menu_verb_button, level_ten_menu_verb2_button, level_ten_menu_verb3_button, level_ten_menu_noun2_button)) 
    
    adventure_button.pack(side='top', pady=5)
    go_back_button.pack(side='top', pady=5)

    l.pack_forget()
    start_button.pack_forget()
    canvas.pack_forget()
    scroll_bar.pack_forget()
    frame.pack_forget()
    go_back_button_2.pack_forget()

def level_one(level_button_1, level_button_2, level_button_3, level_button_4, level_button_5, level_button_6, level_button_7, level_button_8, level_button_9, level_button_10, canvas, frame, scroll_bar, go_back_button_2, adventure_button, go_back_button, l, start_button, level_one_frame, level_two_generate_button, level_two_go_back_button, label_story_level_two, level_two_frame, level_three_generate_button, level_three_go_back_button, level_three_label_story, level_three_menu_adjective_button, level_three_menu_adjective2_button, level_three_menu_noun_button, level_three_menu_noun2_button, level_three_menu_verb_button, level_three_frame, level_four_generate_button, level_four_go_back_button, level_four_story_label, level_four_menu_adjective_button, level_four_menu_noun_button, level_four_menu_verb_button, level_four_menu_noun2_button, level_four_menu_noun3_button, level_four_frame, level_five_generate_button, level_five_go_back_button, level_five_story_label, level_five_frame, level_five_menu_adjective_button, level_five_menu_noun_button, level_five_menu_adverb_button, level_five_menu_verb_button, level_six_go_back_button, level_six_generate_button, level_six_story_label, level_six_frame, level_six_menu_adjective_button, level_six_menu_noun_button, level_six_menu_verb_button, level_six_menu_adjective2_button, level_six_menu_noun2_button, level_six_menu_noun3_button, level_seven_menu_adjective_button, level_seven_menu_noun_button, level_seven_menu_adjective2_button, level_seven_menu_verb_button, level_seven_menu_adjective3_button, level_seven_menu_noun2_button, level_seven_go_back_button, level_seven_generate_button, level_seven_story_label, level_seven_frame, level_eight_go_back_button, level_eight_generate_button, level_eight_story_label, level_eight_frame, level_eight_menu_noun_button, level_eight_menu_adjective_button, level_eight_menu_noun2_button, level_eight_menu_verb_button, level_eight_menu_noun3_button, level_eight_menu_verb2_button, level_eight_menu_adjective2_button, level_eight_menu_noun4_button, level_nine_go_back_button, level_nine_generate_button, level_nine_story_label, level_nine_frame, level_nine_menu_adjective_button, level_nine_menu_noun_button, level_nine_menu_verb_button, level_nine_menu_verb2_button, level_nine_menu_noun2_button, level_ten_go_back_button, level_ten_generate_button, level_ten_story_label, level_ten_frame, level_ten_menu_noun_button, level_ten_menu_verb_button, level_ten_menu_verb2_button, level_ten_menu_verb3_button, level_ten_menu_noun2_button): 
    level_one_frame = tk.Frame(root, width=250, height=200, background='#35393e')
    
    level_button_1.pack_forget()
    level_button_2.pack_forget()
    level_button_3.pack_forget()
    level_button_4.pack_forget()
    level_button_5.pack_forget()
    level_button_6.pack_forget()
    level_button_7.pack_forget()
    level_button_8.pack_forget()
    level_button_9.pack_forget()
    level_button_10.pack_forget()
    canvas.pack_forget()
    scroll_bar.pack_forget()
    frame.pack_forget()
    go_back_button_2.pack_forget()

    def noun_menu(): 
        global menu_noun_button,selected_noun

        selected_noun = tk.StringVar()
        selected_noun.trace("w", lambda *args: menu_selected(selected_noun.get()))

        nouns = ("cat", "dog", "elephant")
        menu_noun_button = ttk.Menubutton(level_one_frame, text="Noun", width=25)
        menu = tk.Menu(menu_noun_button, tearoff=0)

        for noun in nouns: 
            menu.add_radiobutton(label=noun, value=noun, variable=selected_noun)

        menu_noun_button["menu"] = menu
        menu_noun_button.pack(pady=10)

    def noun2_menu(): 
        global menu_noun2_button, selected_noun2

        selected_noun2 = tk.StringVar()
        selected_noun2.trace("w", lambda *args: menu_selected(selected_noun2.get()))

        nouns2 = ("water", "meat", "yarn")
        menu_noun2_button = ttk.Menubutton(level_one_frame, text="Noun", width=25)
        menu = tk.Menu(menu_noun2_button, tearoff=0)

        for noun2 in nouns2: 
            menu.add_radiobutton(label=noun2, value=noun2, variable=selected_noun2)

        menu_noun2_button["menu"] = menu
        menu_noun2_button.pack(pady=10)

    def verb_menu(): 
        global menu_verb_button, selected_verb

        selected_verb = tk.StringVar()
        selected_verb.trace("w", lambda *args: menu_selected(selected_verb.get()))

        verbs = ("drink", "eat", "play")
        menu_verb_button = ttk.Menubutton(level_one_frame, text="Verb", width=25)
        menu = tk.Menu(menu_verb_button, tearoff=0)

        for verb in verbs:
            menu.add_radiobutton(label=verb, value=verb, variable=selected_verb)

        menu_verb_button["menu"] = menu
        menu_verb_button.pack(pady=10)
        
    def adj_menu(): 
        global menu_adj_button, selected_adjective

        selected_adjective = tk.StringVar()
        selected_adjective.trace("w", lambda *args: menu_selected(selected_adjective.get()))

        adjs = ("big", "small", "fat")
        menu_adj_button = ttk.Menubutton(level_one_frame, text="adjective".capitalize(), width=25)
        menu = tk.Menu(menu_adj_button, tearoff=0)

        for adj in adjs: 
            menu.add_radiobutton(label=adj, value=adj, variable=selected_adjective)
        
        menu_adj_button["menu"] = menu
        menu_adj_button.pack(pady=10)

    story = f"Once a upon a time, there was a {adj_menu()} {noun_menu()} who loved to {verb_menu()} with {noun2_menu()}."
    label_story = tk.Label(level_one_frame, text=story)
    label_story.pack(pady=10)

    level_one_frame.pack()

    def menu_selected(): 
        noun_value = selected_noun.get()
        noun2_value = selected_noun2.get()
        verb_value = selected_verb.get()
        adj_value = selected_adjective.get()

        story = f"Once a upon a time, there was a {adj_value} {noun_value} who loved to {verb_value} with {noun2_value}."
        messagebox.showinfo("WordFiller", story)

    generate_level_one_button = tk.Button(level_one_frame, text='generate'.capitalize(), command=menu_selected) 
    generate_level_one_button.pack(pady=10)

    go_back_button_level_one = tk.Button(level_one_frame, text="Go back".upper(), command=lambda: adventure_game(adventure_button, go_back_button, l, start_button, generate_level_one_button, go_back_button_level_one, label_story, level_one_frame, level_two_generate_button, level_two_go_back_button, label_story_level_two, level_two_frame, level_three_generate_button, level_three_go_back_button, level_three_label_story, level_three_menu_adjective_button, level_three_menu_adjective2_button, level_three_menu_noun_button, level_three_menu_noun2_button, level_three_menu_verb_button, level_three_frame, level_four_generate_button, level_four_go_back_button, level_four_story_label, level_four_menu_adjective_button, level_four_menu_noun_button, level_four_menu_verb_button, level_four_menu_noun2_button, level_four_menu_noun3_button, level_four_frame, level_five_generate_button, level_five_go_back_button, level_five_story_label, level_five_frame, level_five_menu_adjective_button, level_five_menu_noun_button, level_five_menu_adverb_button, level_five_menu_verb_button, level_six_go_back_button, level_six_generate_button, level_six_story_label, level_six_frame, level_six_menu_adjective_button, level_six_menu_noun_button, level_six_menu_verb_button, level_six_menu_adjective2_button, level_six_menu_noun2_button, level_six_menu_noun3_button, level_seven_go_back_button, level_seven_generate_button, level_seven_story_label, level_seven_frame, level_seven_menu_adjective_button, level_seven_menu_noun_button, level_seven_menu_adjective2_button, level_seven_menu_verb_button, level_seven_menu_adjective3_button, level_seven_menu_noun2_button, level_eight_go_back_button, level_eight_generate_button, level_eight_story_label, level_eight_frame, level_eight_menu_noun_button, level_eight_menu_adjective_button, level_eight_menu_noun2_button, level_eight_menu_verb_button, level_eight_menu_noun3_button, level_eight_menu_verb2_button, level_eight_menu_adjective2_button, level_eight_menu_noun4_button, level_nine_go_back_button, level_nine_generate_button, level_nine_story_label, level_nine_frame, level_nine_menu_adjective_button, level_nine_menu_noun_button, level_nine_menu_verb_button, level_nine_menu_verb2_button, level_nine_menu_noun2_button, level_ten_go_back_button, level_ten_generate_button, level_ten_story_label, level_ten_frame, level_ten_menu_noun_button, level_ten_menu_verb_button, level_ten_menu_verb2_button, level_ten_menu_verb3_button, level_ten_menu_noun2_button))
    go_back_button_level_one.pack(pady=10)

def level_two(level_button_1, level_button_2, level_button_3, level_button_4, level_button_5, level_button_6, level_button_7, level_button_8, level_button_9, level_button_10, canvas, frame, scroll_bar, quit_button_3, go_back_button_2, adventure_button, go_back_button, l, start_button, quit_button, quit_button2, generate_level_one_button, go_back_button_level_one, label_story, level_one_frame, level_three_menu_adjective_button, level_three_menu_adjective2_button, level_three_menu_noun_button, level_three_menu_noun2_button, level_three_menu_verb_button, level_three_generate_button, level_three_go_back_button, level_three_label_story, level_three_frame, level_four_generate_button, level_four_go_back_button, level_four_story_label, level_four_menu_adjective_button, level_four_menu_noun_button, level_four_menu_verb_button, level_four_menu_noun2_button, level_four_menu_noun3_button, level_four_frame, level_five_generate_button, level_five_go_back_button, level_five_story_label, level_five_frame, level_five_menu_adjective_button, level_five_menu_noun_button, level_five_menu_adverb_button, level_five_menu_verb_button, level_six_go_back_button, level_six_generate_button, level_six_story_label, level_six_frame, level_six_menu_adjective_button, level_six_menu_noun_button, level_six_menu_verb_button, level_six_menu_adjective2_button, level_six_menu_noun2_button, level_six_menu_noun3_button, level_seven_menu_adjective_button, level_seven_menu_noun_button, level_seven_menu_adjective2_button, level_seven_menu_verb_button, level_seven_menu_adjective3_button, level_seven_menu_noun2_button, level_seven_go_back_button, level_seven_generate_button, level_seven_story_label, level_seven_frame, level_eight_go_back_button, level_eight_generate_button, level_eight_story_label, level_eight_frame, level_eight_menu_noun_button, level_eight_menu_adjective_button, level_eight_menu_noun2_button, level_eight_menu_verb_button, level_eight_menu_noun3_button, level_eight_menu_verb2_button, level_eight_menu_adjective2_button, level_eight_menu_noun4_button, level_nine_go_back_button, level_nine_generate_button, level_nine_story_label, level_nine_frame, level_nine_menu_adjective_button, level_nine_menu_noun_button, level_nine_menu_verb_button, level_nine_menu_verb2_button, level_nine_menu_noun2_button, level_ten_go_back_button, level_ten_generate_button, level_ten_story_label, level_ten_frame, level_ten_menu_noun_button, level_ten_menu_verb_button, level_ten_menu_verb2_button, level_ten_menu_verb3_button, level_ten_menu_noun2_button): 
    level_two_frame = tk.Frame(root, width=250, height=200, background='#35393e')

    level_button_1.pack_forget()
    level_button_2.pack_forget()
    level_button_3.pack_forget()
    level_button_4.pack_forget()
    level_button_5.pack_forget()
    level_button_6.pack_forget()
    level_button_7.pack_forget()
    level_button_8.pack_forget()
    level_button_9.pack_forget()
    level_button_10.pack_forget()
    canvas.pack_forget()
    scroll_bar.pack_forget()
    frame.pack_forget()
    go_back_button_2.pack_forget()
    
    def adj_level_two_menu(): 
        global selected_adjective_level_two, level_two_menu_adj_button

        selected_adjective_level_two = tk.StringVar()
        selected_adjective_level_two.trace("w", lambda *args: level_two_menu_selected(selected_adjective_level_two.get()))

        adjs2 = ("loud", "quiet", "crowded")
        level_two_menu_adj_button = ttk.Menubutton(level_two_frame, text="adjective".capitalize(), width=25)
        level_two_menu = tk.Menu(level_two_menu_adj_button, tearoff=0)

        for adj2 in adjs2: 
            level_two_menu.add_radiobutton(label=adj2, value=adj2, variable=selected_adjective_level_two)
        
        level_two_menu_adj_button["menu"] = level_two_menu
        level_two_menu_adj_button.pack(pady=10)

    def adj2_level_two_menu(): 
        global selected_adjective2_level_two, level_two_menu_adj2_button

        selected_adjective2_level_two = tk.StringVar()
        selected_adjective2_level_two.trace("w", lambda *args: level_two_menu_selected(selected_adjective2_level_two.get()))

        adjs2_2 = ("curious", "greedy", "hungry")
        level_two_menu_adj2_button = ttk.Menubutton(level_two_frame, text="adjective".capitalize(), width=25)
        level_two_menu = tk.Menu(level_two_menu_adj2_button, tearoff=0)

        for adj2_2 in adjs2_2: 
            level_two_menu.add_radiobutton(label=adj2_2, value=adj2_2, variable=selected_adjective2_level_two)

        level_two_menu_adj2_button["menu"] = level_two_menu
        level_two_menu_adj2_button.pack(pady=10)

    def noun_level_two_menu(): 
        global selected_noun_level_two, level_two_menu_noun_button

        selected_noun_level_two = tk.StringVar()
        selected_noun_level_two.trace("w", lambda *args: level_two_menu_selected(selected_noun_level_two.get()))

        nouns2_2 = ("racoon", "dog", "lion")
        level_two_menu_noun_button = ttk.Menubutton(level_two_frame, text="noun".capitalize(), width=25)
        level_two_menu = tk.Menu(level_two_menu_noun_button, tearoff=0)

        for noun2_2 in nouns2_2: 
            level_two_menu.add_radiobutton(label=noun2_2, value=noun2_2, variable=selected_noun_level_two)

        level_two_menu_noun_button["menu"] = level_two_menu
        level_two_menu_noun_button.pack(pady=10)

    def verb_level_two_menu(): 
        global selected_verb_level_two, level_two_menu_verb_button

        selected_verb_level_two = tk.StringVar()
        selected_verb_level_two.trace("w", lambda *args: level_two_menu_selected(selected_verb_level_two.get()))

        verbs2 = ("walked", "discovered", "sniffed")
        level_two_menu_verb_button = ttk.Menubutton(level_two_frame, text="verb".capitalize(), width=25)
        level_two_menu = tk.Menu(level_two_menu_verb_button, tearoff=0)

        for verb2 in verbs2: 
            level_two_menu.add_radiobutton(label=verb2, value=verb2, variable=selected_verb_level_two)

        level_two_menu_verb_button["menu"] = level_two_menu
        level_two_menu_verb_button.pack(pady=10)

    def level_two_menu_selected(): 
        level_two_adjective_value = selected_adjective_level_two.get()
        level_two_adjective2_value = selected_adjective2_level_two.get()
        level_two_noun_value = selected_noun_level_two.get()
        level_two_verb_value = selected_verb_level_two.get()

        story2 = f"In a {level_two_adjective_value} village, there lived a {level_two_adjective2_value} {level_two_noun_value} who always {level_two_verb_value} out new adventures."
        messagebox.showinfo("WordFiller", story2)

    level_two_frame.pack()

    story2 = f"In a {adj_level_two_menu()} village, there lived a {adj2_level_two_menu()} {noun_level_two_menu()} who always {verb_level_two_menu()} out new adventures."
    label_story_level_two = tk.Label(level_two_frame, text=story2)
    label_story_level_two.pack(pady=10)

    level_two_generate_button = tk.Button(level_two_frame, text="generate".capitalize(), command=level_two_menu_selected)
    level_two_generate_button.pack(pady=10)

    level_two_go_back_button = tk.Button(level_two_frame, text="Go back".upper(), command=lambda: adventure_game(adventure_button, go_back_button, l, start_button, generate_level_one_button, go_back_button_level_one, label_story, level_one_frame, level_two_generate_button, level_two_go_back_button, label_story_level_two, level_two_frame, level_three_generate_button, level_three_go_back_button, level_three_label_story, level_three_menu_adjective_button, level_three_menu_adjective2_button, level_three_menu_noun_button, level_three_menu_noun2_button, level_three_menu_verb_button, level_three_frame, level_four_generate_button, level_four_go_back_button, level_four_story_label, level_four_menu_adjective_button, level_four_menu_noun_button, level_four_menu_verb_button, level_four_menu_noun2_button, level_four_menu_noun3_button, level_four_frame, level_five_generate_button, level_five_go_back_button, level_five_story_label, level_five_frame, level_five_menu_adjective_button, level_five_menu_noun_button, level_five_menu_adverb_button, level_five_menu_verb_button, level_six_go_back_button, level_six_generate_button, level_six_story_label, level_six_frame, level_six_menu_adjective_button, level_six_menu_noun_button, level_six_menu_verb_button, level_six_menu_adjective2_button, level_six_menu_noun2_button, level_six_menu_noun3_button, level_seven_go_back_button, level_seven_generate_button, level_seven_story_label, level_seven_frame, level_seven_menu_adjective_button, level_seven_menu_noun_button, level_seven_menu_adjective2_button, level_seven_menu_verb_button, level_seven_menu_adjective3_button, level_seven_menu_noun2_button, level_eight_go_back_button, level_eight_generate_button, level_eight_story_label, level_eight_frame, level_eight_menu_noun_button, level_eight_menu_adjective_button, level_eight_menu_noun2_button, level_eight_menu_verb_button, level_eight_menu_noun3_button, level_eight_menu_verb2_button, level_eight_menu_adjective2_button, level_eight_menu_noun4_button, level_nine_go_back_button, level_nine_generate_button, level_nine_story_label, level_nine_frame, level_nine_menu_adjective_button, level_nine_menu_noun_button, level_nine_menu_verb_button, level_nine_menu_verb2_button, level_nine_menu_noun2_button, level_ten_go_back_button, level_ten_generate_button, level_ten_story_label, level_ten_frame, level_ten_menu_noun_button, level_ten_menu_verb_button, level_ten_menu_verb2_button, level_ten_menu_verb3_button, level_ten_menu_noun2_button))
    level_two_go_back_button.pack(pady=10)

def level_three(level_button_1, level_button_2, level_button_3, level_button_4, level_button_5, level_button_6, level_button_7, level_button_8, level_button_9, level_button_10, canvas, frame, go_back_button_2, quit_button_3, scroll_bar, adventure_button, go_back_button, l, start_button, quit_button, quit_button2, generate_level_one_button, go_back_button_level_one, label_story, level_one_frame, level_two_generate_button, level_two_go_back_button, label_story_level_two, level_two_frame, level_three_menu_adjective_button, level_three_menu_adjective2_button, level_three_menu_noun_button, level_three_menu_noun2_button, level_three_menu_verb_button, level_three_frame, level_four_generate_button, level_four_go_back_button, level_four_story_label, level_four_menu_adjective_button, level_four_menu_noun_button, level_four_menu_verb_button, level_four_menu_noun2_button, level_four_menu_noun3_button, level_four_frame, level_five_generate_button, level_five_go_back_button, level_five_story_label, level_five_frame, level_five_menu_adjective_button, level_five_menu_noun_button, level_five_menu_adverb_button, level_five_menu_verb_button, level_six_go_back_button, level_six_generate_button, level_six_story_label, level_six_frame, level_six_menu_adjective_button, level_six_menu_noun_button, level_six_menu_verb_button, level_six_menu_adjective2_button, level_six_menu_noun2_button, level_six_menu_noun3_button, level_seven_menu_adjective_button, level_seven_menu_noun_button, level_seven_menu_adjective2_button, level_seven_menu_verb_button, level_seven_menu_adjective3_button, level_seven_menu_noun2_button, level_seven_go_back_button, level_seven_generate_button, level_seven_story_label, level_seven_frame, level_eight_go_back_button, level_eight_generate_button, level_eight_story_label, level_eight_frame, level_eight_menu_noun_button, level_eight_menu_adjective_button, level_eight_menu_noun2_button, level_eight_menu_verb_button, level_eight_menu_noun3_button, level_eight_menu_verb2_button, level_eight_menu_adjective2_button, level_eight_menu_noun4_button, level_nine_go_back_button, level_nine_generate_button, level_nine_story_label, level_nine_frame, level_nine_menu_adjective_button, level_nine_menu_noun_button, level_nine_menu_verb_button, level_nine_menu_verb2_button, level_nine_menu_noun2_button, level_ten_go_back_button, level_ten_generate_button, level_ten_story_label, level_ten_frame, level_ten_menu_noun_button, level_ten_menu_verb_button, level_ten_menu_verb2_button, level_ten_menu_verb3_button, level_ten_menu_noun2_button): 
    level_three_frame = tk.Frame(root, width=250, height=200, background='#35393e')

    level_button_1.pack_forget()
    level_button_2.pack_forget()
    level_button_3.pack_forget()
    level_button_4.pack_forget()
    level_button_5.pack_forget()
    level_button_6.pack_forget()
    level_button_7.pack_forget()
    level_button_8.pack_forget()
    level_button_9.pack_forget()
    level_button_10.pack_forget()
    canvas.pack_forget()
    scroll_bar.pack_forget()
    frame.pack_forget()
    go_back_button_2.pack_forget()

    def level_three_adjective(): 
        global selected_adjective_level_three, level_three_menu_adjective_button

        selected_adjective_level_three = tk.StringVar()
        selected_adjective_level_three.trace("w", lambda *args: level_three_menu_selected(selected_adjective_level_three.get()))

        adjectives3 = ('cozy', 'beautiful', 'broken')
        level_three_menu_adjective_button = ttk.Menubutton(level_three_frame, text="adjective".capitalize(), width=25)
        level_three_menu = tk.Menu(level_three_menu_adjective_button, tearoff=0)

        for adjective3 in adjectives3: 
            level_three_menu.add_radiobutton(label=adjective3, value=adjective3, variable=selected_adjective_level_three)

        level_three_menu_adjective_button['menu'] = level_three_menu
        level_three_menu_adjective_button.pack(pady=10)

    def level_three_noun(): 
        global selected_noun_level_three, level_three_menu_noun_button

        selected_noun_level_three = tk.StringVar()
        selected_noun_level_three.trace("w", lambda *args: level_three_menu_selected(selected_noun_level_three.get()))

        nouns3 = ("building", "tent", "house")
        level_three_menu_noun_button = ttk.Menubutton(level_three_frame, text='noun'.capitalize(), width=25)
        level_three_menu = tk.Menu(level_three_menu_noun_button, tearoff=0)

        for noun3 in nouns3: 
            level_three_menu.add_radiobutton(label=noun3, value=noun3, variable=selected_noun_level_three)

        level_three_menu_noun_button['menu'] = level_three_menu
        level_three_menu_noun_button.pack(pady=10)

    def level_three_adjective2(): 
        global selected_adjective2_level_three, level_three_menu_adjective2_button

        selected_adjective2_level_three = tk.StringVar()
        selected_adjective2_level_three.trace("w", lambda *args: level_three_menu_selected(selected_adjective2_level_three.get()))

        adjectives3_2 = ("friendly", "funny", "cute")
        level_three_menu_adjective2_button = ttk.Menubutton(level_three_frame, text='adjective'.capitalize(), width=25)
        level_three_menu = tk.Menu(level_three_menu_adjective2_button, tearoff=0)

        for adjective3_2 in adjectives3_2: 
            level_three_menu.add_radiobutton(label=adjective3_2, value=adjective3_2, variable=selected_adjective2_level_three)

        level_three_menu_adjective2_button['menu'] = level_three_menu
        level_three_menu_adjective2_button.pack(pady=10)

    def level_three_verb(): 
        global selected_verb_level_three, level_three_menu_verb_button

        selected_verb_level_three = tk.StringVar()
        selected_verb_level_three.trace("w", lambda *args: level_three_menu_selected(selected_verb_level_three.get()))

        verbs3 = ("brewed", "mixed", "experimented")
        level_three_menu_verb_button = ttk.Menubutton(level_three_frame, text='verb'.capitalize(), width=25)
        level_three_menu = tk.Menu(level_three_menu_verb_button, tearoff=0)

        for verb3 in verbs3: 
            level_three_menu.add_radiobutton(label=verb3, value=verb3, variable=selected_verb_level_three)

        level_three_menu_verb_button['menu'] = level_three_menu
        level_three_menu_verb_button.pack(pady=10)

    def level_three_noun2(): 
        global selected_noun2_level_three, level_three_menu_noun2_button

        selected_noun2_level_three = tk.StringVar()
        selected_noun2_level_three.trace("w", lambda *args: level_three_menu_selected(selected_noun2_level_three.get()))

        nouns3_2 = ("coffee", "tea", "potion")
        level_three_menu_noun2_button = ttk.Menubutton(level_three_frame, text='noun'.capitalize(), width=25)
        level_three_menu = tk.Menu(level_three_menu_noun2_button, tearoff=0)

        for noun3_2 in nouns3_2: 
            level_three_menu.add_radiobutton(label=noun3_2, value=noun3_2, variable=selected_noun2_level_three)

        level_three_menu_noun2_button['menu'] = level_three_menu
        level_three_menu_noun2_button.pack(pady=10)

    def level_three_menu_selected(): 
        level_three_adjective_value = selected_adjective_level_three.get()
        level_three_noun_value = selected_noun_level_three.get()
        level_three_adjective2_value = selected_adjective2_level_three.get()
        level_three_verb_value = selected_verb_level_three.get()
        level_three_noun2_value = selected_noun2_level_three.get()

        story3 = f"Deep in the enchanted forest, there stood a {level_three_adjective_value} {level_three_noun_value} where a {level_three_adjective2_value} witch {level_three_verb_value} a magical {level_three_noun2_value}."
        messagebox.showinfo("WordFiller", story3)

    level_three_frame.pack()

    story3 = f"Deep in the enchanted forest, there stood a {level_three_adjective()} {level_three_noun()} where a {level_three_adjective2()} witch {level_three_verb()} a magical {level_three_noun2()}."
    level_three_label_story = tk.Label(level_three_frame, text=story3, font=(None, 8))
    level_three_label_story.pack(pady=10)

    level_three_generate_button = tk.Button(level_three_frame, text="generate".capitalize(), command=level_three_menu_selected)
    level_three_generate_button.pack(pady=10)

    level_three_go_back_button = tk.Button(level_three_frame, text="Go back".upper(), command=lambda: adventure_game(adventure_button, go_back_button, l, start_button, generate_level_one_button, go_back_button_level_one, label_story, level_one_frame, level_two_generate_button, level_two_go_back_button, label_story_level_two, level_two_frame, level_three_generate_button, level_three_go_back_button, level_three_label_story, level_three_menu_adjective_button, level_three_menu_adjective2_button, level_three_menu_noun_button, level_three_menu_noun2_button, level_three_menu_verb_button, level_three_frame, level_four_generate_button, level_four_go_back_button, level_four_story_label, level_four_menu_adjective_button, level_four_menu_noun_button, level_four_menu_verb_button, level_four_menu_noun2_button, level_four_menu_noun3_button, level_four_frame, level_five_generate_button, level_five_go_back_button, level_five_story_label, level_five_frame, level_five_menu_adjective_button, level_five_menu_noun_button, level_five_menu_adverb_button, level_five_menu_verb_button, level_six_go_back_button, level_six_generate_button, level_six_story_label, level_six_frame, level_six_menu_adjective_button, level_six_menu_noun_button, level_six_menu_verb_button, level_six_menu_adjective2_button, level_six_menu_noun2_button, level_six_menu_noun3_button, level_seven_go_back_button, level_seven_generate_button, level_seven_story_label, level_seven_frame, level_seven_menu_adjective_button, level_seven_menu_noun_button, level_seven_menu_adjective2_button, level_seven_menu_verb_button, level_seven_menu_adjective3_button, level_seven_menu_noun2_button, level_eight_go_back_button, level_eight_generate_button, level_eight_story_label, level_eight_frame, level_eight_menu_noun_button, level_eight_menu_adjective_button, level_eight_menu_noun2_button, level_eight_menu_verb_button, level_eight_menu_noun3_button, level_eight_menu_verb2_button, level_eight_menu_adjective2_button, level_eight_menu_noun4_button, level_nine_go_back_button, level_nine_generate_button, level_nine_story_label, level_nine_frame, level_nine_menu_adjective_button, level_nine_menu_noun_button, level_nine_menu_verb_button, level_nine_menu_verb2_button, level_nine_menu_noun2_button, level_ten_go_back_button, level_ten_generate_button, level_ten_story_label, level_ten_frame, level_ten_menu_noun_button, level_ten_menu_verb_button, level_ten_menu_verb2_button, level_ten_menu_verb3_button, level_ten_menu_noun2_button))
    level_three_go_back_button.pack(pady=10)

def level_four(level_button_1, level_button_2, level_button_3, level_button_4, level_button_5, level_button_6, level_button_7, level_button_8, level_button_9, level_button_10, canvas, scroll_bar, frame, go_back_button_2, quit_button_3, adventure_button, go_back_button, l, start_button, quit_button, quit_button2, generate_level_one_button, go_back_button_level_one, label_story, level_one_frame, level_two_generate_button, level_two_go_back_button, label_story_level_two, level_two_frame, level_three_generate_button, level_three_go_back_button, level_three_label_story, level_four_menu_adjective_button, level_four_menu_noun_button, level_four_menu_verb_button, level_four_menu_noun2_button, level_four_menu_noun3_button, level_three_frame, level_three_menu_adjective_button, level_three_menu_adjective2_button, level_three_menu_noun_button, level_three_menu_noun2_button, level_three_menu_verb_button, level_five_generate_button, level_five_go_back_button, level_five_story_label, level_five_frame, level_five_menu_adjective_button, level_five_menu_noun_button, level_five_menu_adverb_button, level_five_menu_verb_button, level_six_go_back_button, level_six_generate_button, level_six_story_label, level_six_frame, level_six_menu_adjective_button, level_six_menu_noun_button, level_six_menu_verb_button, level_six_menu_adjective2_button, level_six_menu_noun2_button, level_six_menu_noun3_button, level_seven_menu_adjective_button, level_seven_menu_noun_button, level_seven_menu_adjective2_button, level_seven_menu_verb_button, level_seven_menu_adjective3_button, level_seven_menu_noun2_button, level_seven_go_back_button, level_seven_generate_button, level_seven_story_label, level_seven_frame, level_eight_go_back_button, level_eight_generate_button, level_eight_story_label, level_eight_frame, level_eight_menu_noun_button, level_eight_menu_adjective_button, level_eight_menu_noun2_button, level_eight_menu_verb_button, level_eight_menu_noun3_button, level_eight_menu_verb2_button, level_eight_menu_adjective2_button, level_eight_menu_noun4_button, level_nine_go_back_button, level_nine_generate_button, level_nine_story_label, level_nine_frame, level_nine_menu_adjective_button, level_nine_menu_noun_button, level_nine_menu_verb_button, level_nine_menu_verb2_button, level_nine_menu_noun2_button, level_ten_go_back_button, level_ten_generate_button, level_ten_story_label, level_ten_frame, level_ten_menu_noun_button, level_ten_menu_verb_button, level_ten_menu_verb2_button, level_ten_menu_verb3_button, level_ten_menu_noun2_button): 
    level_four_frame = tk.Frame(root, width=250, height=200, background='#35393e')

    level_button_1.pack_forget()
    level_button_2.pack_forget()
    level_button_3.pack_forget()
    level_button_4.pack_forget()
    level_button_5.pack_forget()
    level_button_6.pack_forget()
    level_button_7.pack_forget()
    level_button_8.pack_forget()
    level_button_9.pack_forget()
    level_button_10.pack_forget()
    canvas.pack_forget()
    scroll_bar.pack_forget()
    frame.pack_forget()
    go_back_button_2.pack_forget()

    def level_four_adjective(): 
        global selected_adjective_level_four

        selected_adjective_level_four = tk.StringVar()
        selected_adjective_level_four.trace("w", lambda *args: level_four_menu_selected(selected_adjective_level_four.get()))

        adjectives4 = ("green", "blue", "red")
        level_four_menu_adjective_button = ttk.Menubutton(level_four_frame, text='adjective'.capitalize(), width=25)
        level_four_menu = tk.Menu(level_four_menu_adjective_button, tearoff=0)

        for adjective4 in adjectives4: 
            level_four_menu.add_radiobutton(label=adjective4, value=adjective4, variable=selected_adjective_level_four)

        level_four_menu_adjective_button['menu'] = level_four_menu
        level_four_menu_adjective_button.pack(pady=10)

    def level_four_noun(): 
        global selected_noun_level_four

        selected_noun_level_four = tk.StringVar()
        selected_noun_level_four.trace("w", lambda *args: level_four_menu_selected(selected_noun_level_four.get()))

        nouns4 = ("bus", "car", "aeroplane")
        level_four_menu_noun_button = ttk.Menubutton(level_four_frame, text='noun'.capitalize(), width=25)
        level_four_menu = tk.Menu(level_four_menu_noun_button, tearoff=0)

        for noun4 in nouns4: 
            level_four_menu.add_radiobutton(label=noun4, value=noun4, variable=selected_noun_level_four)

        level_four_menu_noun_button['menu'] = level_four_menu
        level_four_menu_noun_button.pack(pady=10)

    def level_four_verb(): 
        global selected_verb_level_four

        selected_verb_level_four = tk.StringVar()
        selected_verb_level_four.trace("w", lambda *args: level_four_menu_selected(selected_verb_level_four.get()))

        verbs4 = ("raced", "drove", "flew")
        level_four_menu_verb_button = ttk.Menubutton(level_four_frame, text='verb'.capitalize(), width=25)
        level_four_menu = tk.Menu(level_four_menu_verb_button, tearoff=0)

        for verb4 in verbs4: 
            level_four_menu.add_radiobutton(label=verb4, value=verb4, variable=selected_verb_level_four)

        level_four_menu_verb_button['menu'] = level_four_menu
        level_four_menu_verb_button.pack(pady=10)

    def level_four_noun2(): 
        global selected_noun2_level_four

        selected_noun2_level_four = tk.StringVar()
        selected_noun2_level_four.trace("w", lambda *args: level_four_menu_selected(selected_noun2_level_four.get()))

        nouns2 = ("highway", "hill", "mountain")
        level_four_menu_noun2_button = ttk.Menubutton(level_four_frame, text='noun'.capitalize(), width=25)
        level_four_menu = tk.Menu(level_four_menu_noun2_button, tearoff=0)

        for noun2 in nouns2: 
            level_four_menu.add_radiobutton(label=noun2, value=noun2, variable=selected_noun2_level_four)

        level_four_menu_noun2_button['menu'] = level_four_menu
        level_four_menu_noun2_button.pack(pady=10)

    def level_four_noun3(): 
        global selected_noun3_level_four

        selected_noun3_level_four = tk.StringVar()
        selected_noun3_level_four.trace("w", lambda *args: level_four_menu_selected(selected_noun3_level_four.get()))

        nouns3 = ("road", "street", "trail")
        level_four_menu_noun3_button = ttk.Menubutton(level_four_frame, text='noun'.capitalize(), width=25)
        level_four_menu = tk.Menu(level_four_menu_noun3_button, tearoff=0)

        for noun3 in nouns3: 
            level_four_menu.add_radiobutton(label=noun3, value=noun3, variable=selected_noun3_level_four)

        level_four_menu_noun3_button['menu'] = level_four_menu
        level_four_menu_noun3_button.pack(pady=10)

    def level_four_menu_selected(): 
        level_four_adj_value = selected_adjective_level_four.get()
        level_four_noun_value = selected_noun_level_four.get()
        level_four_verb_value = selected_verb_level_four.get()
        level_four_noun2_value = selected_noun2_level_four.get()
        level_four_noun3_value = selected_noun3_level_four.get()

        story4 = f"On a sunny day, a shiny {level_four_adj_value} {level_four_noun_value} {level_four_verb_value} down the {level_four_noun2_value}, leaving a {level_four_noun3_value} of excitement behind."
        messagebox.showinfo("WordFiller", story4)

    level_four_frame.pack()

    story4 = f"On a sunny day, a shiny {level_four_adjective()} {level_four_noun()} {level_four_verb()} down the {level_four_noun2()}, leaving a {level_four_noun3()} of excitement behind."
    level_four_story_label = tk.Label(level_four_frame, text=story4, font=(None, 8))
    level_four_story_label.pack(pady=10)

    level_four_generate_button = tk.Button(level_four_frame, text='generate'.capitalize(), command=level_four_menu_selected)
    level_four_generate_button.pack(pady=10)

    level_four_go_back_button = tk.Button(level_four_frame, text="Go back".upper(), command=lambda: adventure_game(adventure_button, go_back_button, l, start_button, generate_level_one_button, go_back_button_level_one, label_story, level_one_frame, level_two_generate_button, level_two_go_back_button, label_story_level_two, level_two_frame, level_three_generate_button, level_three_go_back_button, level_three_label_story, level_three_menu_adjective_button, level_three_menu_adjective2_button, level_three_menu_noun_button, level_three_menu_noun2_button, level_three_menu_verb_button, level_three_frame, level_four_generate_button, level_four_go_back_button, level_four_story_label, level_four_menu_adjective_button, level_four_menu_noun_button, level_four_menu_verb_button, level_four_menu_noun2_button, level_four_menu_noun3_button, level_four_frame, level_five_generate_button, level_five_go_back_button, level_five_story_label, level_five_frame, level_five_menu_adjective_button, level_five_menu_noun_button, level_five_menu_adverb_button, level_five_menu_verb_button, level_six_go_back_button, level_six_generate_button, level_six_story_label, level_six_frame, level_six_menu_adjective_button, level_six_menu_noun_button, level_six_menu_verb_button, level_six_menu_adjective2_button, level_six_menu_noun2_button, level_six_menu_noun3_button, level_seven_go_back_button, level_seven_generate_button, level_seven_story_label, level_seven_frame, level_seven_menu_adjective_button, level_seven_menu_noun_button, level_seven_menu_adjective2_button, level_seven_menu_verb_button, level_seven_menu_adjective3_button, level_seven_menu_noun2_button, level_eight_go_back_button, level_eight_generate_button, level_eight_story_label, level_eight_frame, level_eight_menu_noun_button, level_eight_menu_adjective_button, level_eight_menu_noun2_button, level_eight_menu_verb_button, level_eight_menu_noun3_button, level_eight_menu_verb2_button, level_eight_menu_adjective2_button, level_eight_menu_noun4_button, level_nine_go_back_button, level_nine_generate_button, level_nine_story_label, level_nine_frame, level_nine_menu_adjective_button, level_nine_menu_noun_button, level_nine_menu_verb_button, level_nine_menu_verb2_button, level_nine_menu_noun2_button, level_ten_go_back_button, level_ten_generate_button, level_ten_story_label, level_ten_frame, level_ten_menu_noun_button, level_ten_menu_verb_button, level_ten_menu_verb2_button, level_ten_menu_verb3_button, level_ten_menu_noun2_button))
    level_four_go_back_button.pack(pady=10)

def level_five(level_button_1, level_button_2, level_button_3, level_button_4, level_button_5, level_button_6, level_button_7, level_button_8, level_button_9, level_button_10, canvas, scroll_bar, frame, quit_button_3, go_back_button_2, adventure_button, go_back_button, l, start_button, quit_button, quit_button2, generate_level_one_button, go_back_button_level_one, label_story, level_one_frame, level_two_generate_button, level_two_go_back_button, label_story_level_two, level_two_frame, level_three_generate_button, level_three_go_back_button, level_three_label_story, level_three_frame, level_four_generate_button, level_four_go_back_button, level_four_story_label, level_four_menu_adjective_button, level_four_menu_noun_button, level_four_menu_verb_button, level_four_menu_noun2_button, level_four_menu_noun3_button, level_four_frame, level_five_generate_button, level_five_go_back_button, level_five_story_label, level_five_frame, level_five_menu_adjective_button, level_five_menu_noun_button, level_five_menu_adverb_button, level_five_menu_verb_button, level_three_menu_adjective_button, level_three_menu_adjective2_button, level_three_menu_noun_button, level_three_menu_noun2_button, level_three_menu_verb_button, level_six_go_back_button, level_six_generate_button, level_six_story_label, level_six_frame, level_six_menu_adjective_button, level_six_menu_noun_button, level_six_menu_verb_button, level_six_menu_adjective2_button, level_six_menu_noun2_button, level_six_menu_noun3_button, level_seven_menu_adjective_button, level_seven_menu_noun_button, level_seven_menu_adjective2_button, level_seven_menu_verb_button, level_seven_menu_adjective3_button, level_seven_menu_noun2_button, level_seven_go_back_button, level_seven_generate_button, level_seven_story_label, level_seven_frame, level_eight_go_back_button, level_eight_generate_button, level_eight_story_label, level_eight_frame, level_eight_menu_noun_button, level_eight_menu_adjective_button, level_eight_menu_noun2_button, level_eight_menu_verb_button, level_eight_menu_noun3_button, level_eight_menu_verb2_button, level_eight_menu_adjective2_button, level_eight_menu_noun4_button, level_nine_go_back_button, level_nine_generate_button, level_nine_story_label, level_nine_frame, level_nine_menu_adjective_button, level_nine_menu_noun_button, level_nine_menu_verb_button, level_nine_menu_verb2_button, level_nine_menu_noun2_button, level_ten_go_back_button, level_ten_generate_button, level_ten_story_label, level_ten_frame, level_ten_menu_noun_button, level_ten_menu_verb_button, level_ten_menu_verb2_button, level_ten_menu_verb3_button, level_ten_menu_noun2_button): 
    level_five_frame = tk.Frame(root, width=250, height=200, background='#35393e')

    level_button_1.pack_forget()
    level_button_2.pack_forget()
    level_button_3.pack_forget()
    level_button_4.pack_forget()
    level_button_5.pack_forget()
    level_button_6.pack_forget()
    level_button_7.pack_forget()
    level_button_8.pack_forget()
    level_button_9.pack_forget()
    level_button_10.pack_forget()
    canvas.pack_forget()
    scroll_bar.pack_forget()
    frame.pack_forget()
    go_back_button_2.pack_forget()

    def level_five_adjective(): 
        global selected_adjective_level_five

        selected_adjective_level_five = tk.StringVar()
        selected_adjective_level_five.trace("w", lambda *args: level_five_menu_selected(selected_adjective_level_five.get()))

        adjectives5 = ("skilled", "talented", "professional")
        level_five_menu_adjective_button = ttk.Menubutton(level_five_frame, text='adjective'.capitalize(), width=25)
        level_five_menu = tk.Menu(level_five_menu_adjective_button, tearoff=0)

        for adjective5 in adjectives5: 
            level_five_menu.add_radiobutton(label=adjective5, value=adjective5, variable=selected_adjective_level_five)

        level_five_menu_adjective_button['menu'] = level_five_menu
        level_five_menu_adjective_button.pack(pady=10)

    def level_five_noun(): 
        global selected_noun_level_five

        selected_noun_level_five = tk.StringVar()
        selected_noun_level_five.trace("w", lambda *args: level_five_menu_selected(selected_noun_level_five.get()))

        nouns5 = ("dancer", "musician", "artist")
        level_five_menu_noun_button = ttk.Menubutton(level_five_frame, text='noun'.capitalize(), width=25)
        level_five_menu = tk.Menu(level_five_menu_noun_button, tearoff=0)

        for noun5 in nouns5: 
            level_five_menu.add_radiobutton(label=noun5, value=noun5, variable=selected_noun_level_five)

        level_five_menu_noun_button['menu'] = level_five_menu
        level_five_menu_noun_button.pack(pady=10)

    def level_five_adverb(): 
        global selected_adverb_level_five

        selected_adverb_level_five = tk.StringVar()
        selected_adverb_level_five.trace("w", lambda *args: level_five_menu_selected(selected_adverb_level_five.get()))

        adverbs5 = ("gracefully", "elegantly", "cautiously")
        level_five_menu_adverb_button = ttk.Menubutton(level_five_frame, text='adverb'.capitalize(), width=25)
        level_five_menu = tk.Menu(level_five_menu_adverb_button, tearoff=0)

        for adverb5 in adverbs5: 
            level_five_menu.add_radiobutton(label=adverb5, value=adverb5, variable=selected_adverb_level_five)

        level_five_menu_adverb_button['menu'] = level_five_menu
        level_five_menu_adverb_button.pack(pady=10)

    def level_five_verb(): 
        global selected_verb_level_five

        selected_verb_level_five = tk.StringVar()
        selected_verb_level_five.trace("w", lambda *args: level_five_menu_selected(selected_verb_level_five.get()))

        verbs5 = ("walked", "proceed", "moved")
        level_five_menu_verb_button = ttk.Menubutton(level_five_frame, text='verb'.capitalize(), width=25)
        level_five_menu = tk.Menu(level_five_menu_verb_button, tearoff=0)

        for verb5 in verbs5: 
            level_five_menu.add_radiobutton(label=verb5, value=verb5, variable=selected_verb_level_five)

        level_five_menu_verb_button['menu'] = level_five_menu
        level_five_menu_verb_button.pack(pady=10)

    def level_five_menu_selected(): 
        level_five_adjective_value = selected_adjective_level_five.get()
        level_five_noun_value = selected_noun_level_five.get()
        level_five_adverb_value = selected_adverb_level_five.get()
        level_five_verb_value = selected_verb_level_five.get()

        story5 = f"In the bustling city, a {level_five_adjective_value} {level_five_noun_value} {level_five_adverb_value} {level_five_verb_value} to the rhythm of the music, captivating the audience."
        messagebox.showinfo("WordFiller", story5)

    level_five_frame.pack()

    story5 = f"In the bustling city, a {level_five_adjective()} {level_five_noun()} {level_five_adverb()} {level_five_verb()} to the rhythm of the music, captivating the audience."
    level_five_story_label = tk.Label(level_five_frame, text=story5, font=(None, 8))
    level_five_story_label.pack(pady=10)

    level_five_generate_button = tk.Button(level_five_frame, text='generate'.capitalize(), command=level_five_menu_selected)
    level_five_generate_button.pack(pady=10)

    level_five_go_back_button = tk.Button(level_five_frame, text='go back'.upper(), command=lambda: adventure_game(adventure_button, go_back_button, l, start_button, generate_level_one_button, go_back_button_level_one, label_story, level_one_frame, level_two_generate_button, level_two_go_back_button, label_story_level_two, level_two_frame, level_three_generate_button, level_three_go_back_button, level_three_label_story, level_three_menu_adjective_button, level_three_menu_adjective2_button, level_three_menu_noun_button, level_three_menu_noun2_button, level_three_menu_verb_button, level_three_frame, level_four_generate_button, level_four_go_back_button, level_four_story_label, level_four_menu_adjective_button, level_four_menu_noun_button, level_four_menu_verb_button, level_four_menu_noun2_button, level_four_menu_noun3_button, level_four_frame, level_five_generate_button, level_five_go_back_button, level_five_story_label, level_five_frame, level_five_menu_adjective_button, level_five_menu_noun_button, level_five_menu_adverb_button, level_five_menu_verb_button, level_six_go_back_button, level_six_generate_button, level_six_story_label, level_six_frame, level_six_menu_adjective_button, level_six_menu_noun_button, level_six_menu_verb_button, level_six_menu_adjective2_button, level_six_menu_noun2_button, level_six_menu_noun3_button, level_seven_go_back_button, level_seven_generate_button, level_seven_story_label, level_seven_frame, level_seven_menu_adjective_button, level_seven_menu_noun_button, level_seven_menu_adjective2_button, level_seven_menu_verb_button, level_seven_menu_adjective3_button, level_seven_menu_noun2_button, level_eight_go_back_button, level_eight_generate_button, level_eight_story_label, level_eight_frame, level_eight_menu_noun_button, level_eight_menu_adjective_button, level_eight_menu_noun2_button, level_eight_menu_verb_button, level_eight_menu_noun3_button, level_eight_menu_verb2_button, level_eight_menu_adjective2_button, level_eight_menu_noun4_button, level_nine_go_back_button, level_nine_generate_button, level_nine_story_label, level_nine_frame, level_nine_menu_adjective_button, level_nine_menu_noun_button, level_nine_menu_verb_button, level_nine_menu_verb2_button, level_nine_menu_noun2_button, level_ten_go_back_button, level_ten_generate_button, level_ten_story_label, level_ten_frame, level_ten_menu_noun_button, level_ten_menu_verb_button, level_ten_menu_verb2_button, level_ten_menu_verb3_button, level_ten_menu_noun2_button))
    level_five_go_back_button.pack(pady=10)

def level_six(level_button_1, level_button_2, level_button_3, level_button_4, level_button_5, level_button_6, level_button_7, level_button_8, level_button_9, level_button_10, canvas, scroll_bar, quit_button_3, go_back_button_2, frame, adventure_button, go_back_button, l, start_button, quit_button, quit_button2, generate_level_one_button, go_back_button_level_one, label_story, level_one_frame, level_two_generate_button, level_two_go_back_button, label_story_level_two, level_two_frame, level_three_generate_button, level_three_go_back_button, level_three_label_story, level_three_menu_adjective_button, level_three_menu_adjective2_button, level_three_menu_noun_button, level_three_menu_noun2_button, level_three_menu_verb_button, level_three_frame, level_four_generate_button, level_four_go_back_button, level_four_story_label, level_four_menu_adjective_button, level_four_menu_noun_button, level_four_menu_verb_button, level_four_menu_noun2_button, level_four_menu_noun3_button, level_four_frame, level_five_generate_button, level_five_go_back_button, level_five_story_label, level_five_frame, level_five_menu_adjective_button, level_five_menu_noun_button, level_five_menu_adverb_button, level_five_menu_verb_button, level_six_menu_adjective_button, level_six_menu_noun_button, level_six_menu_verb_button, level_six_menu_adjective2_button, level_six_menu_noun2_button, level_six_menu_noun3_button, level_seven_menu_adjective_button, level_seven_menu_noun_button, level_seven_menu_adjective2_button, level_seven_menu_verb_button, level_seven_menu_adjective3_button, level_seven_menu_noun2_button, level_seven_go_back_button, level_seven_generate_button, level_seven_story_label, level_seven_frame, level_eight_go_back_button, level_eight_generate_button, level_eight_story_label, level_eight_frame, level_eight_menu_noun_button, level_eight_menu_adjective_button, level_eight_menu_noun2_button, level_eight_menu_verb_button, level_eight_menu_noun3_button, level_eight_menu_verb2_button, level_eight_menu_adjective2_button, level_eight_menu_noun4_button, level_nine_go_back_button, level_nine_generate_button, level_nine_story_label, level_nine_frame, level_nine_menu_adjective_button, level_nine_menu_noun_button, level_nine_menu_verb_button, level_nine_menu_verb2_button, level_nine_menu_noun2_button, level_ten_go_back_button, level_ten_generate_button, level_ten_story_label, level_ten_frame, level_ten_menu_noun_button, level_ten_menu_verb_button, level_ten_menu_verb2_button, level_ten_menu_verb3_button, level_ten_menu_noun2_button): 
    level_six_frame = tk.Frame(root, width=250, height=200, background='#35393e')

    level_button_1.pack_forget()
    level_button_2.pack_forget()
    level_button_3.pack_forget()
    level_button_4.pack_forget()
    level_button_5.pack_forget()
    level_button_6.pack_forget()
    level_button_7.pack_forget()
    level_button_8.pack_forget()
    level_button_9.pack_forget()
    level_button_10.pack_forget()
    canvas.pack_forget()
    scroll_bar.pack_forget()
    frame.pack_forget()
    go_back_button_2.pack_forget()

    def level_six_adjective(): 
        global selected_adjective_level_six

        selected_adjective_level_six = tk.StringVar()
        selected_adjective_level_six.trace("w", lambda *args: level_six_menu_selected(selected_adjective_level_six.get()))

        adjectives6 = ("old", "young", "intelligent")
        level_six_menu_adjective_button = ttk.Menubutton(level_six_frame, text='adjective'.capitalize(), width=25)
        level_six_menu = tk.Menu(level_six_menu_adjective_button, tearoff=0)

        for adjective6 in adjectives6: 
            level_six_menu.add_radiobutton(label=adjective6, value=adjective6, variable=selected_adjective_level_six)
        
        level_six_menu_adjective_button['menu'] = level_six_menu
        level_six_menu_adjective_button.pack(pady=10)

    def level_six_noun(): 
        global selected_noun_level_six

        selected_noun_level_six = tk.StringVar()
        selected_noun_level_six.trace("w", lambda *args: level_six_menu_selected(selected_noun_level_six.get()))

        nouns6 = ("writer", "traveler", "author")
        level_six_menu_noun_button = ttk.Menubutton(level_six_frame, text='noun'.capitalize(), width=25)
        level_six_menu = tk.Menu(level_six_menu_noun_button, tearoff=0)

        for noun6 in nouns6: 
            level_six_menu.add_radiobutton(label=noun6, value=noun6, variable=selected_noun_level_six)

        level_six_menu_noun_button['menu'] = level_six_menu
        level_six_menu_noun_button.pack(pady=10)

    def level_six_verb(): 
        global selected_verb_level_six

        selected_verb_level_six = tk.StringVar()
        selected_verb_level_six.trace("w", lambda *args: level_six_menu_selected(selected_verb_level_six.get()))

        verbs6 = ("created", "crafted", "written")
        level_six_menu_verb_button = ttk.Menubutton(level_six_frame, text='verb'.capitalize(), width=25)
        level_six_menu = tk.Menu(level_six_menu_verb_button, tearoff=0)

        for verb6 in verbs6: 
            level_six_menu.add_radiobutton(label=verb6, value=verb6, variable=selected_verb_level_six)

        level_six_menu_verb_button['menu'] = level_six_menu
        level_six_menu_verb_button.pack(pady=10)

    def level_six_adjective2(): 
        global selected_adjective2_level_six

        selected_adjective2_level_six = tk.StringVar()
        selected_adjective2_level_six.trace("w", lambda *args: level_six_menu_selected(selected_adjective2_level_six.get()))

        adjectives6_2 = ("imaginative", "creative", "inspiring")
        level_six_menu_adjective2_button = ttk.Menubutton(level_six_frame, text='adjective'.capitalize(), width=25)
        level_six_menu = tk.Menu(level_six_menu_adjective2_button, tearoff=0)

        for adjective6_2 in adjectives6_2: 
            level_six_menu.add_radiobutton(label=adjective6_2, value=adjective6_2, variable=selected_adjective2_level_six)

        level_six_menu_adjective2_button['menu'] = level_six_menu
        level_six_menu_adjective2_button.pack(pady=10)

    def level_six_noun2(): 
        global selected_noun2_level_six

        selected_noun2_level_six = tk.StringVar()
        selected_noun2_level_six.trace("w", lambda *args: level_six_menu_selected(selected_noun2_level_six.get()))

        nouns6_2 = ("biographies", "autobiographies", "stories")
        level_six_menu_noun2_button = ttk.Menubutton(level_six_frame, text='noun'.capitalize(), width=25)
        level_six_menu = tk.Menu(level_six_menu_noun2_button, tearoff=0)

        for noun6_2 in nouns6_2: 
            level_six_menu.add_radiobutton(label=noun6_2, value=noun6_2, variable=selected_noun2_level_six)

        level_six_menu_noun2_button['menu'] = level_six_menu
        level_six_menu_noun2_button.pack(pady=10)

    def level_six_noun3(): 
        global selected_noun3_level_six

        selected_noun3_level_six = tk.StringVar()
        selected_noun3_level_six.trace("w", lambda *args: level_six_menu_selected(selected_noun3_level_six.get()))

        nouns6_3 = ("people", "readers", "folks")
        level_six_menu_noun3_button = ttk.Menubutton(level_six_frame, text='noun'.capitalize(), width=25)
        level_six_menu = tk.Menu(level_six_menu_noun3_button, tearoff=0)

        for noun6_3 in nouns6_3: 
            level_six_menu.add_radiobutton(label=noun6_3, value=noun6_3, variable=selected_noun3_level_six)

        level_six_menu_noun3_button['menu'] = level_six_menu
        level_six_menu_noun3_button.pack(pady=10)

    def level_six_menu_selected(): 
        level_six_adjective_value = selected_adjective_level_six.get()
        level_six_noun_value = selected_noun_level_six.get()
        level_six_verb_value = selected_verb_level_six.get()
        level_six_adjective2_value = selected_adjective2_level_six.get()
        level_six_noun2_value = selected_noun2_level_six.get()
        level_six_noun3_value = selected_noun3_level_six.get()

        story6 = f"Lost in a world of books, a {level_six_adjective_value} {level_six_noun_value} {level_six_verb_value} {level_six_adjective2_value} {level_six_noun2_value} that transported {level_six_noun3_value} to far-off lands."
        messagebox.showinfo("WordFiller", story6)

    level_six_frame.pack()

    story6 = f"Lost in a world of books, a {level_six_adjective()} {level_six_noun()} {level_six_verb()} {level_six_adjective2()} {level_six_noun2()} that transported {level_six_noun3()} to far-off lands."
    level_six_story_label = tk.Label(level_six_frame, text=story6, font=(None, 8))
    level_six_story_label.pack(pady=10)

    level_six_generate_button = tk.Button(level_six_frame, text='generate'.capitalize(), command=level_six_menu_selected)
    level_six_generate_button.pack(pady=10)

    level_six_go_back_button = tk.Button(level_six_frame, text='go back'.upper(), command=lambda: adventure_game(adventure_button, go_back_button, l, start_button, generate_level_one_button, go_back_button_level_one, label_story, level_one_frame, level_two_generate_button, level_two_go_back_button, label_story_level_two, level_two_frame, level_three_generate_button, level_three_go_back_button, level_three_label_story, level_three_menu_adjective_button, level_three_menu_adjective2_button, level_three_menu_noun_button, level_three_menu_noun2_button, level_three_menu_verb_button, level_three_frame, level_four_generate_button, level_four_go_back_button, level_four_story_label, level_four_menu_adjective_button, level_four_menu_noun_button, level_four_menu_verb_button, level_four_menu_noun2_button, level_four_menu_noun3_button, level_four_frame, level_five_generate_button, level_five_go_back_button, level_five_story_label, level_five_frame, level_five_menu_adjective_button, level_five_menu_noun_button, level_five_menu_adverb_button, level_five_menu_verb_button, level_six_go_back_button, level_six_generate_button, level_six_story_label, level_six_frame, level_six_menu_adjective_button, level_six_menu_noun_button, level_six_menu_verb_button, level_six_menu_adjective2_button, level_six_menu_noun2_button, level_six_menu_noun3_button, level_seven_go_back_button, level_seven_generate_button, level_seven_story_label, level_seven_frame, level_seven_menu_adjective_button, level_seven_menu_noun_button, level_seven_menu_adjective2_button, level_seven_menu_verb_button, level_seven_menu_adjective3_button, level_seven_menu_noun2_button, level_eight_go_back_button, level_eight_generate_button, level_eight_story_label, level_eight_frame, level_eight_menu_noun_button, level_eight_menu_adjective_button, level_eight_menu_noun2_button, level_eight_menu_verb_button, level_eight_menu_noun3_button, level_eight_menu_verb2_button, level_eight_menu_adjective2_button, level_eight_menu_noun4_button, level_nine_go_back_button, level_nine_generate_button, level_nine_story_label, level_nine_frame, level_nine_menu_adjective_button, level_nine_menu_noun_button, level_nine_menu_verb_button, level_nine_menu_verb2_button, level_nine_menu_noun2_button, level_ten_go_back_button, level_ten_generate_button, level_ten_story_label, level_ten_frame, level_ten_menu_noun_button, level_ten_menu_verb_button, level_ten_menu_verb2_button, level_ten_menu_verb3_button, level_ten_menu_noun2_button))
    level_six_go_back_button.pack(pady=10)

def level_seven(level_button_1, level_button_2, level_button_3, level_button_4, level_button_5, level_button_6, level_button_7, level_button_8, level_button_9, level_button_10, canvas, scroll_bar, quit_button_3, go_back_button_2, frame, adventure_button, go_back_button, l, start_button, quit_button, quit_button2, generate_level_one_button, go_back_button_level_one, label_story, level_one_frame, level_two_generate_button, level_two_go_back_button, label_story_level_two, level_two_frame, level_three_generate_button, level_three_go_back_button, level_three_label_story, level_three_menu_adjective_button, level_three_menu_adjective2_button, level_three_menu_noun_button, level_three_menu_noun2_button, level_three_menu_verb_button, level_three_frame, level_four_generate_button, level_four_go_back_button, level_four_story_label, level_four_menu_adjective_button, level_four_menu_noun_button, level_four_menu_verb_button, level_four_menu_noun2_button, level_four_menu_noun3_button, level_four_frame, level_five_generate_button, level_five_go_back_button, level_five_story_label, level_five_frame, level_five_menu_adjective_button, level_five_menu_noun_button, level_five_menu_adverb_button, level_five_menu_verb_button, level_six_menu_adjective_button, level_six_menu_noun_button, level_six_menu_verb_button, level_six_menu_adjective2_button, level_six_menu_noun2_button, level_six_menu_noun3_button, level_seven_menu_adjective_button, level_seven_menu_noun_button, level_seven_menu_adjective2_button, level_seven_menu_verb_button, level_seven_menu_adjective3_button, level_seven_menu_noun2_button, level_six_go_back_button, level_six_generate_button, level_six_story_label, level_six_frame, level_eight_go_back_button, level_eight_generate_button, level_eight_story_label, level_eight_frame, level_eight_menu_noun_button, level_eight_menu_adjective_button, level_eight_menu_noun2_button, level_eight_menu_verb_button, level_eight_menu_noun3_button, level_eight_menu_verb2_button, level_eight_menu_adjective2_button, level_eight_menu_noun4_button, level_nine_go_back_button, level_nine_generate_button, level_nine_story_label, level_nine_frame, level_nine_menu_adjective_button, level_nine_menu_noun_button, level_nine_menu_verb_button, level_nine_menu_verb2_button, level_nine_menu_noun2_button, level_ten_go_back_button, level_ten_generate_button, level_ten_story_label, level_ten_frame, level_ten_menu_noun_button, level_ten_menu_verb_button, level_ten_menu_verb2_button, level_ten_menu_verb3_button, level_ten_menu_noun2_button): 
    level_seven_frame = tk.Frame(root, width=250, height=200, background='#35393e')

    level_button_1.pack_forget()
    level_button_2.pack_forget()
    level_button_3.pack_forget()
    level_button_4.pack_forget()
    level_button_5.pack_forget()
    level_button_6.pack_forget()
    level_button_7.pack_forget()
    level_button_8.pack_forget()
    level_button_9.pack_forget()
    level_button_10.pack_forget()
    canvas.pack_forget()
    scroll_bar.pack_forget()
    frame.pack_forget()
    go_back_button_2.pack_forget()

    def level_seven_adjective(): 
        global selected_adjective_level_seven

        selected_adjective_level_seven = tk.StringVar()
        selected_adjective_level_seven.trace("w", lambda *args: level_seven_selected_menu(selected_adjective_level_seven.get()))

        adjectives7 = ("timid", "courageous", "determined")
        level_seven_menu_adjective_button = ttk.Menubutton(level_seven_frame, text='adjective'.capitalize(), width=25)
        level_seven_menu = tk.Menu(level_seven_menu_adjective_button, tearoff=0)

        for adjective7 in adjectives7: 
            level_seven_menu.add_radiobutton(label=adjective7, value=adjective7, variable=selected_adjective_level_seven)

        level_seven_menu_adjective_button['menu'] = level_seven_menu
        level_seven_menu_adjective_button.pack(pady=10)

    def level_seven_noun(): 
        global selected_noun_level_seven

        selected_noun_level_seven = tk.StringVar()
        selected_noun_level_seven.trace("w", lambda *args: level_seven_selected_menu(selected_noun_level_seven.get()))

        nouns7 = ("knight", "hero", "prince")
        level_seven_menu_noun_button = ttk.Menubutton(level_seven_frame, text='noun'.capitalize(), width=25)
        level_seven_menu = tk.Menu(level_seven_menu_noun_button, tearoff=0)

        for noun7 in nouns7: 
            level_seven_menu.add_radiobutton(label=noun7, value=noun7, variable=selected_noun_level_seven)

        level_seven_menu_noun_button['menu'] = level_seven_menu
        level_seven_menu_noun_button.pack(pady=10)

    def level_seven_adjective2(): 
        global selected_adjective2_level_seven

        selected_adjective2_level_seven = tk.StringVar()
        selected_adjective2_level_seven.trace("w", lambda *args: level_seven_selected_menu(selected_adjective2_level_seven.get()))

        adjectives7_2 = ("daring", "dangerous", "challenging")
        level_seven_menu_adjective2_button = ttk.Menubutton(level_seven_frame, text='adjective'.capitalize(), width=25)
        level_seven_menu = tk.Menu(level_seven_menu_adjective2_button, tearoff=0)

        for adjective7_2 in adjectives7_2: 
            level_seven_menu.add_radiobutton(label=adjective7_2, value=adjective7_2, variable=selected_adjective2_level_seven)

        level_seven_menu_adjective2_button['menu'] = level_seven_menu
        level_seven_menu_adjective2_button.pack(pady=10)

    def level_seven_verb(): 
        global selected_verb_level_seven

        selected_verb_level_seven = tk.StringVar()
        selected_verb_level_seven.trace("w", lambda *args: level_seven_selected_menu(selected_verb_level_seven.get()))

        verbs7 = ("rescue", "help", "free")
        level_seven_menu_verb_button = ttk.Menubutton(level_seven_frame, text='verb'.capitalize(), width=25)
        level_seven_menu = tk.Menu(level_seven_menu_verb_button, tearoff=0)

        for verb7 in verbs7: 
            level_seven_menu.add_radiobutton(label=verb7, value=verb7, variable=selected_verb_level_seven)

        level_seven_menu_verb_button['menu'] = level_seven_menu
        level_seven_menu_verb_button.pack(pady=10)

    def level_seven_adjective3(): 
        global selected_adjective3_level_seven

        selected_adjective3_level_seven = tk.StringVar()
        selected_adjective3_level_seven.trace("w", lambda *args: level_seven_selected_menu(selected_adjective3_level_seven.get()))

        adjectives7_3 = ("captured", "lively", "exquisite")
        level_seven_menu_adjective3_button = ttk.Menubutton(level_seven_frame, text='adjective'.capitalize(), width=25)
        level_seven_menu = tk.Menu(level_seven_menu_adjective3_button, tearoff=0)

        for adjective7_3 in adjectives7_3: 
            level_seven_menu.add_radiobutton(label=adjective7_3, value=adjective7_3, variable=selected_adjective3_level_seven)

        level_seven_menu_adjective3_button['menu'] = level_seven_menu
        level_seven_menu_adjective3_button.pack(pady=10)

    def level_seven_noun2(): 
        global selected_noun2_level_seven

        selected_noun2_level_seven = tk.StringVar()
        selected_noun2_level_seven.trace("w", lambda *args: level_seven_selected_menu(selected_noun2_level_seven.get()))

        nouns7_2 = ("dinosaur", "pterodactyl", "dragon")
        level_seven_menu_noun2_button = ttk.Menubutton(level_seven_frame, text='noun'.capitalize(), width=25)
        level_seven_menu = tk.Menu(level_seven_menu_noun2_button, tearoff=0)

        for noun7_2 in nouns7_2: 
            level_seven_menu.add_radiobutton(label=noun7_2, value=noun7_2, variable=selected_noun2_level_seven)

        level_seven_menu_noun2_button['menu'] = level_seven_menu
        level_seven_menu_noun2_button.pack(pady=10)

    def level_seven_selected_menu(): 
        level_seven_adjective_value = selected_adjective_level_seven.get()
        level_seven_noun_value = selected_noun_level_seven.get()
        level_seven_adjective2_value = selected_adjective2_level_seven.get()
        level_seven_verb_value = selected_verb_level_seven.get()
        level_seven_adjective3_value = selected_adjective3_level_seven.get()
        level_seven_noun2_value = selected_noun2_level_seven.get()

        story7 = f"On a stormy night, a {level_seven_adjective_value} {level_seven_noun_value} set out on a {level_seven_adjective2_value} quest to {level_seven_verb_value} a {level_seven_adjective3_value} princess from a fearsome {level_seven_noun2_value}."
        messagebox.showinfo("WordFiller", story7)

    level_seven_frame.pack()

    story7 = f"On a stormy night, a {level_seven_adjective()} {level_seven_noun()} set out on a {level_seven_adjective2()} quest to {level_seven_verb()} a {level_seven_adjective3()} princess from a fearsome {level_seven_noun2()}."
    level_seven_story_label = tk.Label(level_seven_frame, text=story7, font=(None, 7))
    level_seven_story_label.pack(pady=10)

    level_seven_generate_button = tk.Button(level_seven_frame, text='generate'.capitalize(), command=level_seven_selected_menu)
    level_seven_generate_button.pack(pady=10)

    level_seven_go_back_button = tk.Button(level_seven_frame, text='go back'.upper(), command=lambda: adventure_game(adventure_button, go_back_button, l, start_button, generate_level_one_button, go_back_button_level_one, label_story, level_one_frame, level_two_generate_button, level_two_go_back_button, label_story_level_two, level_two_frame, level_three_generate_button, level_three_go_back_button, level_three_label_story, level_three_menu_adjective_button, level_three_menu_adjective2_button, level_three_menu_noun_button, level_three_menu_noun2_button, level_three_menu_verb_button, level_three_frame, level_four_generate_button, level_four_go_back_button, level_four_story_label, level_four_menu_adjective_button, level_four_menu_noun_button, level_four_menu_verb_button, level_four_menu_noun2_button, level_four_menu_noun3_button, level_four_frame, level_five_generate_button, level_five_go_back_button, level_five_story_label, level_five_frame, level_five_menu_adjective_button, level_five_menu_noun_button, level_five_menu_adverb_button, level_five_menu_verb_button, level_six_go_back_button, level_six_generate_button, level_six_story_label, level_six_frame, level_six_menu_adjective_button, level_six_menu_noun_button, level_six_menu_verb_button, level_six_menu_adjective2_button, level_six_menu_noun2_button, level_six_menu_noun3_button, level_seven_go_back_button, level_seven_generate_button, level_seven_story_label, level_seven_frame, level_seven_menu_adjective_button, level_seven_menu_noun_button, level_seven_menu_adjective2_button, level_seven_menu_verb_button, level_seven_menu_adjective3_button, level_seven_menu_noun2_button, level_eight_go_back_button, level_eight_generate_button, level_eight_story_label, level_eight_frame, level_eight_menu_noun_button, level_eight_menu_adjective_button, level_eight_menu_noun2_button, level_eight_menu_verb_button, level_eight_menu_noun3_button, level_eight_menu_verb2_button, level_eight_menu_adjective2_button, level_eight_menu_noun4_button, level_nine_go_back_button, level_nine_generate_button, level_nine_story_label, level_nine_frame, level_nine_menu_adjective_button, level_nine_menu_noun_button, level_nine_menu_verb_button, level_nine_menu_verb2_button, level_nine_menu_noun2_button, level_ten_go_back_button, level_ten_generate_button, level_ten_story_label, level_ten_frame, level_ten_menu_noun_button, level_ten_menu_verb_button, level_ten_menu_verb2_button, level_ten_menu_verb3_button, level_ten_menu_noun2_button))
    level_seven_go_back_button.pack(pady=10)

def level_eight(level_button_1, level_button_2, level_button_3, level_button_4, level_button_5, level_button_6, level_button_7, level_button_8, level_button_9, level_button_10, canvas, scroll_bar, quit_button_3, go_back_button_2, frame, adventure_button, go_back_button, l, start_button, quit_button, quit_button2, generate_level_one_button, go_back_button_level_one, label_story, level_one_frame, level_two_generate_button, level_two_go_back_button, label_story_level_two, level_two_frame, level_three_generate_button, level_three_go_back_button, level_three_label_story, level_three_menu_adjective_button, level_three_menu_adjective2_button, level_three_menu_noun_button, level_three_menu_noun2_button, level_three_menu_verb_button, level_three_frame, level_four_generate_button, level_four_go_back_button, level_four_story_label, level_four_menu_adjective_button, level_four_menu_noun_button, level_four_menu_verb_button, level_four_menu_noun2_button, level_four_menu_noun3_button, level_four_frame, level_five_generate_button, level_five_go_back_button, level_five_story_label, level_five_frame, level_five_menu_adjective_button, level_five_menu_noun_button, level_five_menu_adverb_button, level_five_menu_verb_button, level_six_menu_adjective_button, level_six_menu_noun_button, level_six_menu_verb_button, level_six_menu_adjective2_button, level_six_menu_noun2_button, level_six_menu_noun3_button, level_seven_menu_adjective_button, level_seven_menu_noun_button, level_seven_menu_adjective2_button, level_seven_menu_verb_button, level_seven_menu_adjective3_button, level_seven_menu_noun2_button, level_six_go_back_button, level_six_generate_button, level_six_story_label, level_six_frame, level_eight_menu_noun_button, level_eight_menu_adjective_button, level_eight_menu_noun2_button, level_eight_menu_verb_button, level_eight_menu_noun3_button, level_eight_menu_verb2_button, level_eight_menu_adjective2_button, level_eight_menu_noun4_button, level_seven_go_back_button, level_seven_generate_button, level_seven_story_label, level_seven_frame, level_nine_go_back_button, level_nine_generate_button, level_nine_story_label, level_nine_frame, level_nine_menu_adjective_button, level_nine_menu_noun_button, level_nine_menu_verb_button, level_nine_menu_verb2_button, level_nine_menu_noun2_button, level_ten_go_back_button, level_ten_generate_button, level_ten_story_label, level_ten_frame, level_ten_menu_noun_button, level_ten_menu_verb_button, level_ten_menu_verb2_button, level_ten_menu_verb3_button, level_ten_menu_noun2_button): 
    level_eight_frame = tk.Frame(root, width=250, height=200, background='#35393e')

    level_button_1.pack_forget()
    level_button_2.pack_forget()
    level_button_3.pack_forget()
    level_button_4.pack_forget()
    level_button_5.pack_forget()
    level_button_6.pack_forget()
    level_button_7.pack_forget()
    level_button_8.pack_forget()
    level_button_9.pack_forget()
    level_button_10.pack_forget()
    canvas.pack_forget()
    scroll_bar.pack_forget()
    frame.pack_forget()
    go_back_button_2.pack_forget()

    def level_eight_noun(): 
        global selected_noun_level_eight

        selected_noun_level_eight = tk.StringVar()
        selected_noun_level_eight.trace("w", lambda *args: level_eight_selected_menu(selected_noun_level_eight.get()))

        nouns8 = ("imps", "goblins", "fairies")
        level_eight_menu_noun_button = ttk.Menubutton(level_eight_frame, text='noun'.capitalize(), width=25)
        level_eight_menu = tk.Menu(level_eight_menu_noun_button, tearoff=0)

        for noun8 in nouns8: 
            level_eight_menu.add_radiobutton(label=noun8, value=noun8, variable=selected_noun_level_eight)

        level_eight_menu_noun_button['menu'] = level_eight_menu
        level_eight_menu_noun_button.pack(pady=10)

    def level_eight_adjective(): 
        global selected_adjective_level_eight

        selected_adjective_level_eight = tk.StringVar()
        selected_adjective_level_eight.trace("w", lambda *args: level_eight_selected_menu(selected_adjective_level_eight.get()))

        adjectives8 = ("terrifying", "mischievous", "vicious")
        level_eight_menu_adjective_button = ttk.Menubutton(level_eight_frame, text='adjective'.capitalize(), width=25)
        level_eight_menu = tk.Menu(level_eight_menu_adjective_button, tearoff=0)

        for adjective8 in adjectives8: 
            level_eight_menu.add_radiobutton(label=adjective8, value=adjective8, variable=selected_adjective_level_eight)

        level_eight_menu_adjective_button['menu'] = level_eight_menu
        level_eight_menu_adjective_button.pack(pady=10)

    def level_eight_noun2(): 
        global selected_noun2_level_eight

        selected_noun2_level_eight = tk.StringVar()
        selected_noun2_level_eight.trace("w", lambda *args: level_eight_selected_menu(selected_noun2_level_eight.get()))

        nouns8_2 = ("sprite", "hobgoblin", "pixie")
        level_eight_menu_noun2_button = ttk.Menubutton(level_eight_frame, text='noun'.capitalize(), width=25)
        level_eight_menu = tk.Menu(level_eight_menu_noun2_button, tearoff=0)

        for noun8_2 in nouns8_2: 
            level_eight_menu.add_radiobutton(label=noun8_2, value=noun8_2, variable=selected_noun2_level_eight)

        level_eight_menu_noun2_button['menu'] = level_eight_menu
        level_eight_menu_noun2_button.pack(pady=10)

    def level_eight_verb(): 
        global selected_verb_level_eight

        selected_verb_level_eight = tk.StringVar()
        selected_verb_level_eight.trace("w", lambda *args: level_eight_selected_menu(selected_verb_level_eight.get()))

        verbs8 = ("cast", "diffuse", "emit")
        level_eight_menu_verb_button = ttk.Menubutton(level_eight_frame, text='verb'.capitalize(), width=25)
        level_eight_menu = tk.Menu(level_eight_menu_verb_button, tearoff=0)

        for verb8 in verbs8: 
            level_eight_menu.add_radiobutton(label=verb8, value=verb8, variable=selected_verb_level_eight)

        level_eight_menu_verb_button['menu'] = level_eight_menu
        level_eight_menu_verb_button.pack(pady=10)

    def level_eight_noun3(): 
        global selected_noun3_level_eight

        selected_noun3_level_eight = tk.StringVar()
        selected_noun3_level_eight.trace("w", lambda *args: level_eight_selected_menu(selected_noun3_level_eight.get()))

        nouns8_3 = ("hexes", "magics", "spells")
        level_eight_menu_noun3_button = ttk.Menubutton(level_eight_frame, text='noun'.capitalize(), width=25)
        level_eight_menu = tk.Menu(level_eight_menu_noun3_button, tearoff=0)

        for noun8_3 in nouns8_3: 
            level_eight_menu.add_radiobutton(label=noun8_3, value=noun8_3, variable=selected_noun3_level_eight)

        level_eight_menu_noun3_button['menu'] = level_eight_menu
        level_eight_menu_noun3_button.pack(pady=10)

    def level_eight_verb2(): 
        global selected_verb2_level_eight

        selected_verb2_level_eight = tk.StringVar()
        selected_verb2_level_eight.trace("w", lambda *args: level_eight_selected_menu(selected_verb2_level_eight.get()))

        verbs8_2 = ("created", "caused", "generated")
        level_eight_menu_verb2_button = ttk.Menubutton(level_eight_frame, text='verb'.capitalize(), width=25)
        level_eight_menu = tk.Menu(level_eight_menu_verb2_button, tearoff=0)

        for verb8_2 in verbs8_2: 
            level_eight_menu.add_radiobutton(label=verb8_2, value=verb8_2, variable=selected_verb2_level_eight)

        level_eight_menu_verb2_button['menu'] = level_eight_menu
        level_eight_menu_verb2_button.pack(pady=10)

    def level_eight_adjective2(): 
        global selected_adjective2_level_eight

        selected_adjective2_level_eight = tk.StringVar()
        selected_adjective2_level_eight.trace("w", lambda *args: level_eight_selected_menu(selected_adjective2_level_eight.get()))

        adjectives8_2 = ("exuberant", "playful", "spirited")
        level_eight_menu_adjective2_button = ttk.Menubutton(level_eight_frame, text='adjective'.capitalize(), width=25)
        level_eight_menu = tk.Menu(level_eight_menu_adjective2_button, tearoff=0)

        for adjective8_2 in adjectives8_2: 
            level_eight_menu.add_radiobutton(label=adjective8_2, value=adjective8_2, variable=selected_adjective2_level_eight)

        level_eight_menu_adjective2_button['menu'] = level_eight_menu
        level_eight_menu_adjective2_button.pack(pady=10)

    def level_eight_noun4(): 
        global selected_noun4_level_eight 

        selected_noun4_level_eight = tk.StringVar()
        selected_noun4_level_eight.trace("w", lambda *args: level_eight_selected_menu(selected_noun4_level_eight.get()))

        nouns8_4 = ("chaos", "pandemonium", "mayhem")
        level_eight_menu_noun4_button = ttk.Menubutton(level_eight_frame, text='noun'.capitalize(), width=25)
        level_eight_menu = tk.Menu(level_eight_menu_noun4_button, tearoff=0)

        for noun8_4 in nouns8_4: 
            level_eight_menu.add_radiobutton(label=noun8_4, value=noun8_4, variable=selected_noun4_level_eight)

        level_eight_menu_noun4_button['menu'] = level_eight_menu
        level_eight_menu_noun4_button.pack(pady=10)

    def level_eight_selected_menu(): 
        level_eight_noun_value = selected_noun_level_eight.get()
        level_eight_adjective_value = selected_adjective_level_eight.get()
        level_eight_noun2_value = selected_noun2_level_eight.get()
        level_eight_verb_value = selected_verb_level_eight.get()
        level_eight_noun3_value = selected_noun3_level_eight.get()
        level_eight_verb2_value = selected_verb2_level_eight.get()
        level_eight_adjective2_value = selected_adjective2_level_eight.get()
        level_eight_noun4_value = selected_noun4_level_eight.get()

        story8 = f"In the mystical realm of {level_eight_noun_value}, a {level_eight_adjective_value} {level_eight_noun2_value} {level_eight_verb_value} {level_eight_noun3_value} and {level_eight_verb2_value} {level_eight_adjective2_value} {level_eight_noun4_value} wherever it went."
        messagebox.showinfo("WordFiller", story8)

    level_eight_frame.pack()

    story8 = f"In the mystical realm of {level_eight_noun()}, a {level_eight_adjective()} {level_eight_noun2()} {level_eight_verb()} {level_eight_noun3()} and {level_eight_verb2()} {level_eight_adjective2()} {level_eight_noun4()} wherever it went."
    level_eight_story_label = tk.Label(level_eight_frame, text=story8, font=(None, 8))
    level_eight_story_label.pack(pady=10)

    level_eight_generate_button = tk.Button(level_eight_frame, text='generate'.capitalize(), command=level_eight_selected_menu)
    level_eight_generate_button.pack(pady=10)

    level_eight_go_back_button = tk.Button(level_eight_frame, text='go back'.upper(), command=lambda: adventure_game(adventure_button, go_back_button, l, start_button, generate_level_one_button, go_back_button_level_one, label_story, level_one_frame, level_two_generate_button, level_two_go_back_button, label_story_level_two, level_two_frame, level_three_generate_button, level_three_go_back_button, level_three_label_story, level_three_menu_adjective_button, level_three_menu_adjective2_button, level_three_menu_noun_button, level_three_menu_noun2_button, level_three_menu_verb_button, level_three_frame, level_four_generate_button, level_four_go_back_button, level_four_story_label, level_four_menu_adjective_button, level_four_menu_noun_button, level_four_menu_verb_button, level_four_menu_noun2_button, level_four_menu_noun3_button, level_four_frame, level_five_generate_button, level_five_go_back_button, level_five_story_label, level_five_frame, level_five_menu_adjective_button, level_five_menu_noun_button, level_five_menu_adverb_button, level_five_menu_verb_button, level_six_go_back_button, level_six_generate_button, level_six_story_label, level_six_frame, level_six_menu_adjective_button, level_six_menu_noun_button, level_six_menu_verb_button, level_six_menu_adjective2_button, level_six_menu_noun2_button, level_six_menu_noun3_button, level_seven_go_back_button, level_seven_generate_button, level_seven_story_label, level_seven_frame, level_seven_menu_adjective_button, level_seven_menu_noun_button, level_seven_menu_adjective2_button, level_seven_menu_verb_button, level_seven_menu_adjective3_button, level_seven_menu_noun2_button, level_eight_go_back_button, level_eight_generate_button, level_eight_story_label, level_eight_frame, level_eight_menu_noun_button, level_eight_menu_adjective_button, level_eight_menu_noun2_button, level_eight_menu_verb_button, level_eight_menu_noun3_button, level_eight_menu_verb2_button, level_eight_menu_adjective2_button, level_eight_menu_noun4_button, level_nine_go_back_button, level_nine_generate_button, level_nine_story_label, level_nine_frame, level_nine_menu_adjective_button, level_nine_menu_noun_button, level_nine_menu_verb_button, level_nine_menu_verb2_button, level_nine_menu_noun2_button, level_ten_go_back_button, level_ten_generate_button, level_ten_story_label, level_ten_frame, level_ten_menu_noun_button, level_ten_menu_verb_button, level_ten_menu_verb2_button, level_ten_menu_verb3_button, level_ten_menu_noun2_button))
    level_eight_go_back_button.pack(pady=10)

def level_nine(level_button_1, level_button_2, level_button_3, level_button_4, level_button_5, level_button_6, level_button_7, level_button_8, level_button_9, level_button_10, canvas, scroll_bar, quit_button_3, go_back_button_2, frame, adventure_button, go_back_button, l, start_button, quit_button, quit_button2, generate_level_one_button, go_back_button_level_one, label_story, level_one_frame, level_two_generate_button, level_two_go_back_button, label_story_level_two, level_two_frame, level_three_generate_button, level_three_go_back_button, level_three_label_story, level_three_menu_adjective_button, level_three_menu_adjective2_button, level_three_menu_noun_button, level_three_menu_noun2_button, level_three_menu_verb_button, level_three_frame, level_four_generate_button, level_four_go_back_button, level_four_story_label, level_four_menu_adjective_button, level_four_menu_noun_button, level_four_menu_verb_button, level_four_menu_noun2_button, level_four_menu_noun3_button, level_four_frame, level_five_generate_button, level_five_go_back_button, level_five_story_label, level_five_frame, level_five_menu_adjective_button, level_five_menu_noun_button, level_five_menu_adverb_button, level_five_menu_verb_button, level_six_menu_adjective_button, level_six_menu_noun_button, level_six_menu_verb_button, level_six_menu_adjective2_button, level_six_menu_noun2_button, level_six_menu_noun3_button, level_seven_menu_adjective_button, level_seven_menu_noun_button, level_seven_menu_adjective2_button, level_seven_menu_verb_button, level_seven_menu_adjective3_button, level_seven_menu_noun2_button, level_six_go_back_button, level_six_generate_button, level_six_story_label, level_six_frame, level_eight_menu_noun_button, level_eight_menu_adjective_button, level_eight_menu_noun2_button, level_eight_menu_verb_button, level_eight_menu_noun3_button, level_eight_menu_verb2_button, level_eight_menu_adjective2_button, level_eight_menu_noun4_button, level_seven_go_back_button, level_seven_generate_button, level_seven_story_label, level_seven_frame, level_nine_go_back_button, level_nine_generate_button, level_nine_story_label, level_nine_frame, level_nine_menu_adjective_button, level_nine_menu_noun_button, level_nine_menu_verb_button, level_nine_menu_verb2_button, level_nine_menu_noun2_button, level_eight_go_back_button, level_eight_generate_button, level_eight_story_label, level_eight_frame, level_ten_go_back_button, level_ten_generate_button, level_ten_story_label, level_ten_frame, level_ten_menu_noun_button, level_ten_menu_verb_button, level_ten_menu_verb2_button, level_ten_menu_verb3_button, level_ten_menu_noun2_button): 
    level_nine_frame = tk.Frame(root, width=250, height=200, background='#35393e')

    level_button_1.pack_forget()
    level_button_2.pack_forget()
    level_button_3.pack_forget()
    level_button_4.pack_forget()
    level_button_5.pack_forget()
    level_button_6.pack_forget()
    level_button_7.pack_forget()
    level_button_8.pack_forget()
    level_button_9.pack_forget()
    level_button_10.pack_forget()
    canvas.pack_forget()
    scroll_bar.pack_forget()
    frame.pack_forget()
    go_back_button_2.pack_forget()

    def level_nine_adjective(): 
        global selected_adjective_level_nine

        selected_adjective_level_nine = tk.StringVar()
        selected_adjective_level_nine.trace("w", lambda *args: level_nine_menu_selected(selected_adjective_level_nine.get()))

        adjectives9 = ("gifted", "brilliant", "innovative")
        level_nine_menu_adjective_button = ttk.Menubutton(level_nine_frame, text='adjective'.capitalize(), width=25)
        level_nine_menu = tk.Menu(level_nine_menu_adjective_button, tearoff=0)

        for adjective9 in adjectives9: 
            level_nine_menu.add_radiobutton(label=adjective9, value=adjective9, variable=selected_adjective_level_nine)

        level_nine_menu_adjective_button['menu'] = level_nine_menu
        level_nine_menu_adjective_button.pack(pady=10)

    def level_nine_noun(): 
        global selected_noun_level_nine

        selected_noun_level_nine = tk.StringVar()
        selected_noun_level_nine.trace("w", lambda *args: level_nine_menu_selected(selected_noun_level_nine.get()))

        nouns9 = ("scientist", "innovator", "astronomer")
        level_nine_menu_noun_button = ttk.Menubutton(level_nine_frame, text='noun'.capitalize(), width=25)
        level_nine_menu = tk.Menu(level_nine_menu_noun_button, tearoff=0)

        for noun9 in nouns9: 
            level_nine_menu.add_radiobutton(label=noun9, value=noun9, variable=selected_noun_level_nine)

        level_nine_menu_noun_button['menu'] = level_nine_menu
        level_nine_menu_noun_button.pack(pady=10)

    def level_nine_verb(): 
        global selected_verb_level_nine

        selected_verb_level_nine = tk.StringVar()
        selected_verb_level_nine.trace("w", lambda *args: level_nine_menu_selected(selected_verb_level_nine.get()))

        verbs9 = ("innovated", "invented", "originated")
        level_nine_menu_verb_button = ttk.Menubutton(level_nine_frame, text='verb'.capitalize(), width=25)
        level_nine_menu = tk.Menu(level_nine_menu_verb_button, tearoff=0)

        for verb9 in verbs9: 
            level_nine_menu.add_radiobutton(label=verb9, value=verb9, variable=selected_verb_level_nine)

        level_nine_menu_verb_button['menu'] = level_nine_menu
        level_nine_menu_verb_button.pack(pady=10)

    def level_nine_verb2(): 
        global selected_verb2_level_nine

        selected_verb2_level_nine = tk.StringVar()
        selected_verb2_level_nine.trace("w", lambda *args: level_nine_menu_selected(selected_verb2_level_nine.get()))

        verbs9_2 = ("unseal", "free", "unlock")
        level_nine_menu_verb2_button = ttk.Menubutton(level_nine_frame, text='verb'.capitalize(), width=25)
        level_nine_menu = tk.Menu(level_nine_menu_verb2_button, tearoff=0)

        for verb9_2 in verbs9_2: 
            level_nine_menu.add_radiobutton(label=verb9_2, value=verb9_2, variable=selected_verb2_level_nine)

        level_nine_menu_verb2_button['menu'] = level_nine_menu
        level_nine_menu_verb2_button.pack(pady=10)

    def level_nine_noun2(): 
        global selected_noun2_level_nine

        selected_noun2_level_nine = tk.StringVar()
        selected_noun2_level_nine.trace("w", lambda *args: level_nine_menu_selected(selected_noun2_level_nine.get()))

        nouns9_2 = ("mysteries", "puzzles", "secrets")
        level_nine_menu_noun2_button = ttk.Menubutton(level_nine_frame, text='noun'.capitalize(), width=25)
        level_nine_menu = tk.Menu(level_nine_menu_noun2_button, tearoff=0)

        for noun9_2 in nouns9_2: 
            level_nine_menu.add_radiobutton(label=noun9_2, value=noun9_2, variable=selected_noun2_level_nine)

        level_nine_menu_noun2_button['menu'] = level_nine_menu
        level_nine_menu_noun2_button.pack(pady=10)

    def level_nine_menu_selected(): 
        level_nine_adjective_value = selected_adjective_level_nine.get()
        level_nine_noun_value = selected_noun_level_nine.get()
        level_nine_verb_value = selected_verb_level_nine.get()
        level_nine_verb2_value = selected_verb2_level_nine.get()
        level_nine_noun2_value = selected_noun2_level_nine.get()

        story9 = f"In a distant galaxy, a {level_nine_adjective_value} {level_nine_noun_value} {level_nine_verb_value} a time machine that could {level_nine_verb2_value} the {level_nine_noun2_value} of the universe."
        messagebox.showinfo("WordFiller", story9)

    level_nine_frame.pack()

    story9 = f"In a distant galaxy, a {level_nine_adjective()} {level_nine_noun()} {level_nine_verb()} a time machine that could {level_nine_verb2()} the {level_nine_noun2()} of the universe."
    level_nine_story_label = tk.Label(level_nine_frame, text=story9, font=(None, 8))
    level_nine_story_label.pack(pady=10)

    level_nine_generate_button = tk.Button(level_nine_frame, text='generate'.capitalize(), command=level_nine_menu_selected)
    level_nine_generate_button.pack(pady=10)

    level_nine_go_back_button = tk.Button(level_nine_frame, text='go back'.upper(), command=lambda: adventure_game(adventure_button, go_back_button, l, start_button, generate_level_one_button, go_back_button_level_one, label_story, level_one_frame, level_two_generate_button, level_two_go_back_button, label_story_level_two, level_two_frame, level_three_generate_button, level_three_go_back_button, level_three_label_story, level_three_menu_adjective_button, level_three_menu_adjective2_button, level_three_menu_noun_button, level_three_menu_noun2_button, level_three_menu_verb_button, level_three_frame, level_four_generate_button, level_four_go_back_button, level_four_story_label, level_four_menu_adjective_button, level_four_menu_noun_button, level_four_menu_verb_button, level_four_menu_noun2_button, level_four_menu_noun3_button, level_four_frame, level_five_generate_button, level_five_go_back_button, level_five_story_label, level_five_frame, level_five_menu_adjective_button, level_five_menu_noun_button, level_five_menu_adverb_button, level_five_menu_verb_button, level_six_go_back_button, level_six_generate_button, level_six_story_label, level_six_frame, level_six_menu_adjective_button, level_six_menu_noun_button, level_six_menu_verb_button, level_six_menu_adjective2_button, level_six_menu_noun2_button, level_six_menu_noun3_button, level_seven_go_back_button, level_seven_generate_button, level_seven_story_label, level_seven_frame, level_seven_menu_adjective_button, level_seven_menu_noun_button, level_seven_menu_adjective2_button, level_seven_menu_verb_button, level_seven_menu_adjective3_button, level_seven_menu_noun2_button, level_eight_go_back_button, level_eight_generate_button, level_eight_story_label, level_eight_frame, level_eight_menu_noun_button, level_eight_menu_adjective_button, level_eight_menu_noun2_button, level_eight_menu_verb_button, level_eight_menu_noun3_button, level_eight_menu_verb2_button, level_eight_menu_adjective2_button, level_eight_menu_noun4_button, level_nine_go_back_button, level_nine_generate_button, level_nine_story_label, level_nine_frame, level_nine_menu_adjective_button, level_nine_menu_noun_button, level_nine_menu_verb_button, level_nine_menu_verb2_button, level_nine_menu_noun2_button, level_ten_go_back_button, level_ten_generate_button, level_ten_story_label, level_ten_frame, level_ten_menu_noun_button, level_ten_menu_verb_button, level_ten_menu_verb2_button, level_ten_menu_verb3_button, level_ten_menu_noun2_button))
    level_nine_go_back_button.pack(pady=10)

def level_ten(level_button_1, level_button_2, level_button_3, level_button_4, level_button_5, level_button_6, level_button_7, level_button_8, level_button_9, level_button_10, canvas, scroll_bar, quit_button_3, go_back_button_2, frame, adventure_button, go_back_button, l, start_button, quit_button, quit_button2, generate_level_one_button, go_back_button_level_one, label_story, level_one_frame, level_two_generate_button, level_two_go_back_button, label_story_level_two, level_two_frame, level_three_generate_button, level_three_go_back_button, level_three_label_story, level_three_menu_adjective_button, level_three_menu_adjective2_button, level_three_menu_noun_button, level_three_menu_noun2_button, level_three_menu_verb_button, level_three_frame, level_four_generate_button, level_four_go_back_button, level_four_story_label, level_four_menu_adjective_button, level_four_menu_noun_button, level_four_menu_verb_button, level_four_menu_noun2_button, level_four_menu_noun3_button, level_four_frame, level_five_generate_button, level_five_go_back_button, level_five_story_label, level_five_frame, level_five_menu_adjective_button, level_five_menu_noun_button, level_five_menu_adverb_button, level_five_menu_verb_button, level_six_menu_adjective_button, level_six_menu_noun_button, level_six_menu_verb_button, level_six_menu_adjective2_button, level_six_menu_noun2_button, level_six_menu_noun3_button, level_seven_menu_adjective_button, level_seven_menu_noun_button, level_seven_menu_adjective2_button, level_seven_menu_verb_button, level_seven_menu_adjective3_button, level_seven_menu_noun2_button, level_six_go_back_button, level_six_generate_button, level_six_story_label, level_six_frame, level_eight_menu_noun_button, level_eight_menu_adjective_button, level_eight_menu_noun2_button, level_eight_menu_verb_button, level_eight_menu_noun3_button, level_eight_menu_verb2_button, level_eight_menu_adjective2_button, level_eight_menu_noun4_button, level_seven_go_back_button, level_seven_generate_button, level_seven_story_label, level_seven_frame, level_nine_go_back_button, level_nine_generate_button, level_nine_story_label, level_nine_frame, level_nine_menu_adjective_button, level_nine_menu_noun_button, level_nine_menu_verb_button, level_nine_menu_verb2_button, level_nine_menu_noun2_button, level_eight_go_back_button, level_eight_generate_button, level_eight_story_label, level_eight_frame, level_ten_menu_noun_button, level_ten_menu_verb_button, level_ten_menu_verb2_button, level_ten_menu_verb3_button, level_ten_menu_noun2_button): 
    level_ten_frame = tk.Frame(root, width=250, height=200, background='#35393e')

    level_button_1.pack_forget()
    level_button_2.pack_forget()
    level_button_3.pack_forget()
    level_button_4.pack_forget()
    level_button_5.pack_forget()
    level_button_6.pack_forget()
    level_button_7.pack_forget()
    level_button_8.pack_forget()
    level_button_9.pack_forget()
    level_button_10.pack_forget()
    canvas.pack_forget()
    scroll_bar.pack_forget()
    frame.pack_forget()
    go_back_button_2.pack_forget()

    def level_ten_noun(): 
        global selected_noun_level_ten

        selected_noun_level_ten = tk.StringVar()
        selected_noun_level_ten.trace("w", lambda *args: level_ten_menu_selected(selected_noun_level_ten.get()))

        nouns10 = ("remanants", "survivors", "people")
        level_ten_menu_noun_button = ttk.Menubutton(level_ten_frame, text='noun'.capitalize(), width=25)
        level_ten_menu = tk.Menu(level_ten_menu_noun_button, tearoff=0)

        for noun10 in nouns10: 
            level_ten_menu.add_radiobutton(label=noun10, value=noun10, variable=selected_noun_level_ten)

        level_ten_menu_noun_button['menu'] = level_ten_menu
        level_ten_menu_noun_button.pack(pady=10)

    def level_ten_verb(): 
        global selected_verb_level_ten

        selected_verb_level_ten = tk.StringVar()
        selected_verb_level_ten.trace("w", lambda *args: level_ten_menu_selected(selected_verb_level_ten.get()))

        verbs10 = ("cooperate", "collaborate", "banded")
        level_ten_menu_verb_button = ttk.Menubutton(level_ten_frame, text='verb'.capitalize(), width=25)
        level_ten_menu = tk.Menu(level_ten_menu_verb_button, tearoff=0)

        for verb10 in verbs10: 
            level_ten_menu.add_radiobutton(label=verb10, value=verb10, variable=selected_verb_level_ten)

        level_ten_menu_verb_button['menu'] = level_ten_menu
        level_ten_menu_verb_button.pack(pady=10)

    def level_ten_verb2(): 
        global selected_verb2_level_ten

        selected_verb2_level_ten = tk.StringVar()
        selected_verb2_level_ten.trace("w", lambda *args: level_ten_menu_selected(selected_verb2_level_ten.get()))

        verbs10_2 = ("renovate", "reconstruct", "rebuild")
        level_ten_menu_verb2_button = ttk.Menubutton(level_ten_frame, text='verb'.capitalize(), width=25)
        level_ten_menu = tk.Menu(level_ten_menu_verb2_button, tearoff=0)

        for verb10_2 in verbs10_2: 
            level_ten_menu.add_radiobutton(label=verb10_2, value=verb10_2, variable=selected_verb2_level_ten)

        level_ten_menu_verb2_button['menu'] = level_ten_menu
        level_ten_menu_verb2_button.pack(pady=10)

    def level_ten_noun2():
        global selected_noun2_level_ten

        selected_noun2_level_ten = tk.StringVar()
        selected_noun2_level_ten.trace("w", lambda *args: level_ten_menu_selected(selected_noun2_level_ten.get()))
        
        nouns10_2 = ("enlightenment", "cultivation", "civilisation")
        level_ten_menu_noun2_button = ttk.Menubutton(level_ten_frame, text='noun'.capitalize(), width=25)
        level_ten_menu = tk.Menu(level_ten_menu_noun2_button, tearoff=0)

        for noun10_2 in nouns10_2: 
            level_ten_menu.add_radiobutton(label=noun10_2, value=noun10_2, variable=selected_noun2_level_ten)

        level_ten_menu_noun2_button['menu'] = level_ten_menu
        level_ten_menu_noun2_button.pack(pady=10)

    def level_ten_verb3(): 
        global selected_verb3_level_ten

        selected_verb3_level_ten = tk.StringVar()
        selected_verb3_level_ten.trace("w", lambda *args: level_ten_menu_selected(selected_verb3_level_ten.get()))

        verbs10_3 = ("restore", "rehabilitate", "modernise")
        level_ten_menu_verb3_button = ttk.Menubutton(level_ten_frame, text='verb'.capitalize(), width=25)
        level_ten_menu = tk.Menu(level_ten_menu_verb3_button, tearoff=0)

        for verb10_3 in verbs10_3: 
            level_ten_menu.add_radiobutton(label=verb10_3, value=verb10_3, variable=selected_verb3_level_ten)

        level_ten_menu_verb3_button['menu'] = level_ten_menu
        level_ten_menu_verb3_button.pack(pady=10)

    def level_ten_menu_selected(): 
        level_ten_noun_value = selected_noun_level_ten.get()
        level_ten_verb_value = selected_verb_level_ten.get()
        level_ten_verb2_value = selected_verb2_level_ten.get()
        level_ten_noun2_value = selected_noun2_level_ten.get()
        level_ten_verb3_value = selected_verb3_level_ten.get()

        story10 = f"In the post-apocalyptic world, a group of {level_ten_noun_value} {level_ten_verb_value} together to {level_ten_verb2_value} {level_ten_noun2_value} and {level_ten_verb3_value} hope for the future."
        messagebox.showinfo("WordFiller", story10)

    level_ten_frame.pack()

    story10 = f"In the post-apocalyptic world, a group of {level_ten_noun()} {level_ten_verb()} together to {level_ten_verb2()} {level_ten_noun2()} and {level_ten_verb3()} hope for the future."
    level_ten_story_label = tk.Label(level_ten_frame, text=story10, font=(None, 7))
    level_ten_story_label.pack(pady=10)

    level_ten_generate_button = tk.Button(level_ten_frame, text='generate'.capitalize(), command=level_ten_menu_selected)
    level_ten_generate_button.pack(pady=10)

    level_ten_go_back_button = tk.Button(level_ten_frame, text='go back'.upper(), command=lambda: adventure_game(adventure_button, go_back_button, l, start_button, generate_level_one_button, go_back_button_level_one, label_story, level_one_frame, level_two_generate_button, level_two_go_back_button, label_story_level_two, level_two_frame, level_three_generate_button, level_three_go_back_button, level_three_label_story, level_three_menu_adjective_button, level_three_menu_adjective2_button, level_three_menu_noun_button, level_three_menu_noun2_button, level_three_menu_verb_button, level_three_frame, level_four_generate_button, level_four_go_back_button, level_four_story_label, level_four_menu_adjective_button, level_four_menu_noun_button, level_four_menu_verb_button, level_four_menu_noun2_button, level_four_menu_noun3_button, level_four_frame, level_five_generate_button, level_five_go_back_button, level_five_story_label, level_five_frame, level_five_menu_adjective_button, level_five_menu_noun_button, level_five_menu_adverb_button, level_five_menu_verb_button, level_six_go_back_button, level_six_generate_button, level_six_story_label, level_six_frame, level_six_menu_adjective_button, level_six_menu_noun_button, level_six_menu_verb_button, level_six_menu_adjective2_button, level_six_menu_noun2_button, level_six_menu_noun3_button, level_seven_go_back_button, level_seven_generate_button, level_seven_story_label, level_seven_frame, level_seven_menu_adjective_button, level_seven_menu_noun_button, level_seven_menu_adjective2_button, level_seven_menu_verb_button, level_seven_menu_adjective3_button, level_seven_menu_noun2_button, level_eight_go_back_button, level_eight_generate_button, level_eight_story_label, level_eight_frame, level_eight_menu_noun_button, level_eight_menu_adjective_button, level_eight_menu_noun2_button, level_eight_menu_verb_button, level_eight_menu_noun3_button, level_eight_menu_verb2_button, level_eight_menu_adjective2_button, level_eight_menu_noun4_button, level_nine_go_back_button, level_nine_generate_button, level_nine_story_label, level_nine_frame, level_nine_menu_adjective_button, level_nine_menu_noun_button, level_nine_menu_verb_button, level_nine_menu_verb2_button, level_nine_menu_noun2_button, level_ten_go_back_button, level_ten_generate_button, level_ten_story_label, level_ten_frame, level_ten_menu_noun_button, level_ten_menu_verb_button, level_ten_menu_verb2_button, level_ten_menu_verb3_button, level_ten_menu_noun2_button))
    level_ten_go_back_button.pack(pady=10)

def adventure_game(adventure_button, go_back_button, l, start_button, generate_level_one_button, go_back_button_level_one, label_story, level_one_frame, level_two_generate_button, level_two_go_back_button, label_story_level_two, level_two_frame, level_three_generate_button, level_three_go_back_button, level_three_label_story, level_three_menu_adjective_button, level_three_menu_adjective2_button, level_three_menu_noun_button, level_three_menu_noun2_button, level_three_menu_verb_button, level_three_frame, level_four_generate_button, level_four_go_back_button, level_four_story_label, level_four_menu_adjective_button, level_four_menu_noun_button, level_four_menu_verb_button, level_four_menu_noun2_button, level_four_menu_noun3_button, level_four_frame, level_five_generate_button, level_five_go_back_button, level_five_story_label, level_five_frame, level_five_menu_adjective_button, level_five_menu_noun_button, level_five_menu_adverb_button, level_five_menu_verb_button, level_six_go_back_button, level_six_generate_button, level_six_story_label, level_six_frame, level_six_menu_adjective_button, level_six_menu_noun_button, level_six_menu_verb_button, level_six_menu_adjective2_button, level_six_menu_noun2_button, level_six_menu_noun3_button, level_seven_go_back_button, level_seven_generate_button, level_seven_story_label, level_seven_frame, level_seven_menu_adjective_button, level_seven_menu_noun_button, level_seven_menu_adjective2_button, level_seven_menu_verb_button, level_seven_menu_adjective3_button, level_seven_menu_noun2_button, level_eight_go_back_button, level_eight_generate_button, level_eight_story_label, level_eight_frame, level_eight_menu_noun_button, level_eight_menu_adjective_button, level_eight_menu_noun2_button, level_eight_menu_verb_button, level_eight_menu_noun3_button, level_eight_menu_verb2_button, level_eight_menu_adjective2_button, level_eight_menu_noun4_button, level_nine_go_back_button, level_nine_generate_button, level_nine_story_label, level_nine_frame, level_nine_menu_adjective_button, level_nine_menu_noun_button, level_nine_menu_verb_button, level_nine_menu_verb2_button, level_nine_menu_noun2_button, level_ten_go_back_button, level_ten_generate_button, level_ten_story_label, level_ten_frame, level_ten_menu_noun_button, level_ten_menu_verb_button, level_ten_menu_verb2_button, level_ten_menu_verb3_button, level_ten_menu_noun2_button): 
    canvas = tk.Canvas(root, width=250, height=200, background='#35393e')
    canvas.pack(side='left', fill='both', expand=1)

    scroll_bar = tk.Scrollbar(root, orient='vertical', command=canvas.yview)
    scroll_bar.pack(side='right', fill='y')

    canvas.configure(yscrollcommand=scroll_bar.set)

    frame = tk.Frame(canvas, background='#35393e')
    canvas.create_window((0, 0), window=frame, anchor='nw')

    go_back_button_2 = tk.Button(frame, text='Go Back'.upper(), width=25, height=5, pady=10, background='#5D6064', command=lambda: start_game(l, start_button, canvas, scroll_bar, frame, go_back_button_2, generate_level_one_button, go_back_button_level_one, label_story, level_one_frame, level_two_generate_button, level_two_go_back_button, label_story_level_two, level_two_frame, level_three_generate_button, level_three_go_back_button, level_three_label_story, level_three_menu_adjective_button, level_three_menu_adjective2_button, level_three_menu_noun_button, level_three_menu_noun2_button, level_three_menu_verb_button, level_three_frame, level_four_generate_button, level_four_go_back_button, level_four_story_label, level_four_menu_adjective_button, level_four_menu_noun_button, level_four_menu_verb_button, level_four_menu_noun2_button, level_four_menu_noun3_button, level_four_frame, level_five_generate_button, level_five_go_back_button, level_five_story_label, level_five_frame, level_five_menu_adjective_button, level_five_menu_noun_button, level_five_menu_adverb_button, level_five_menu_verb_button, level_six_go_back_button, level_six_generate_button, level_six_story_label, level_six_frame, level_six_menu_adjective_button, level_six_menu_noun_button, level_six_menu_verb_button, level_six_menu_adjective2_button, level_six_menu_noun2_button, level_six_menu_noun3_button, level_seven_menu_adjective_button, level_seven_menu_noun_button, level_seven_menu_adjective2_button, level_seven_menu_verb_button, level_seven_menu_adjective3_button, level_seven_menu_noun2_button, level_seven_go_back_button, level_seven_generate_button, level_seven_story_label, level_seven_frame, level_eight_go_back_button, level_eight_generate_button, level_eight_story_label, level_eight_frame, level_eight_menu_noun_button, level_eight_menu_adjective_button, level_eight_menu_noun2_button, level_eight_menu_verb_button, level_eight_menu_noun3_button, level_eight_menu_verb2_button, level_eight_menu_adjective2_button, level_eight_menu_noun4_button, level_nine_go_back_button, level_nine_generate_button, level_nine_story_label, level_nine_frame, level_nine_menu_adjective_button, level_nine_menu_noun_button, level_nine_menu_verb_button, level_nine_menu_verb2_button, level_nine_menu_noun2_button, level_ten_go_back_button, level_ten_generate_button, level_ten_story_label, level_ten_frame, level_ten_menu_noun_button, level_ten_menu_verb_button, level_ten_menu_verb2_button, level_ten_menu_verb3_button, level_ten_menu_noun2_button))

    go_back_button_2.pack(side='top')
 
    level_button_1 = tk.Button(frame, text="level 1".upper(), width=25, height=5, pady=10, background='#5D6064', font=("Bauhaus 93", 16), fg='#CAF1DE', command=lambda: level_one(level_button_1, level_button_2, level_button_3, level_button_4, level_button_5, level_button_6, level_button_7, level_button_8, level_button_9, level_button_10, canvas, frame, scroll_bar, go_back_button_2, adventure_button, go_back_button, l, start_button, level_one_frame, level_two_generate_button, level_two_go_back_button, label_story_level_two, level_two_frame, level_three_generate_button, level_three_go_back_button, level_three_label_story, level_three_menu_adjective_button, level_three_menu_adjective2_button, level_three_menu_noun_button, level_three_menu_noun2_button, level_three_menu_verb_button, level_three_frame, level_four_generate_button, level_four_go_back_button, level_four_story_label, level_four_menu_adjective_button, level_four_menu_noun_button, level_four_menu_verb_button, level_four_menu_noun2_button, level_four_menu_noun3_button, level_four_frame, level_five_generate_button, level_five_go_back_button, level_five_story_label, level_five_frame, level_five_menu_adjective_button, level_five_menu_noun_button, level_five_menu_adverb_button, level_five_menu_verb_button, level_six_go_back_button, level_six_generate_button, level_six_story_label, level_six_frame, level_six_menu_adjective_button, level_six_menu_noun_button, level_six_menu_verb_button, level_six_menu_adjective2_button, level_six_menu_noun2_button, level_six_menu_noun3_button, level_seven_menu_adjective_button, level_seven_menu_noun_button, level_seven_menu_adjective2_button, level_seven_menu_verb_button, level_seven_menu_adjective3_button, level_seven_menu_noun2_button, level_seven_go_back_button, level_seven_generate_button, level_seven_story_label, level_seven_frame, level_eight_go_back_button, level_eight_generate_button, level_eight_story_label, level_eight_frame, level_eight_menu_noun_button, level_eight_menu_adjective_button, level_eight_menu_noun2_button, level_eight_menu_verb_button, level_eight_menu_noun3_button, level_eight_menu_verb2_button, level_eight_menu_adjective2_button, level_eight_menu_noun4_button, level_nine_go_back_button, level_nine_generate_button, level_nine_story_label, level_nine_frame, level_nine_menu_adjective_button, level_nine_menu_noun_button, level_nine_menu_verb_button, level_nine_menu_verb2_button, level_nine_menu_noun2_button, level_ten_go_back_button, level_ten_generate_button, level_ten_story_label, level_ten_frame, level_ten_menu_noun_button, level_ten_menu_verb_button, level_ten_menu_verb2_button, level_ten_menu_verb3_button, level_ten_menu_noun2_button))
    level_button_2 = tk.Button(frame, text="level 2".upper(), width=25, height=5, pady=10, background='#5D6064', font=("Bauhaus 93", 16), fg='#CAF1DE', command=lambda: level_two(level_button_1, level_button_2, level_button_3, level_button_4, level_button_5, level_button_6, level_button_7, level_button_8, level_button_9, level_button_10, canvas, frame, scroll_bar, go_back_button_2, adventure_button, go_back_button, l, start_button, generate_level_one_button, go_back_button_level_one, label_story, level_one_frame, level_three_menu_adjective_button, level_three_menu_adjective2_button, level_three_menu_noun_button, level_three_menu_noun2_button, level_three_menu_verb_button, level_three_generate_button, level_three_go_back_button, level_three_label_story, level_three_frame, level_four_generate_button, level_four_go_back_button, level_four_story_label, level_four_menu_adjective_button, level_four_menu_noun_button, level_four_menu_verb_button, level_four_menu_noun2_button, level_four_menu_noun3_button, level_four_frame, level_five_generate_button, level_five_go_back_button, level_five_story_label, level_five_frame, level_five_menu_adjective_button, level_five_menu_noun_button, level_five_menu_adverb_button, level_five_menu_verb_button, level_six_go_back_button, level_six_generate_button, level_six_story_label, level_six_frame, level_six_menu_adjective_button, level_six_menu_noun_button, level_six_menu_verb_button, level_six_menu_adjective2_button, level_six_menu_noun2_button, level_six_menu_noun3_button, level_seven_menu_adjective_button, level_seven_menu_noun_button, level_seven_menu_adjective2_button, level_seven_menu_verb_button, level_seven_menu_adjective3_button, level_seven_menu_noun2_button, level_seven_go_back_button, level_seven_generate_button, level_seven_story_label, level_seven_frame, level_eight_go_back_button, level_eight_generate_button, level_eight_story_label, level_eight_frame, level_eight_menu_noun_button, level_eight_menu_adjective_button, level_eight_menu_noun2_button, level_eight_menu_verb_button, level_eight_menu_noun3_button, level_eight_menu_verb2_button, level_eight_menu_adjective2_button, level_eight_menu_noun4_button, level_nine_go_back_button, level_nine_generate_button, level_nine_story_label, level_nine_frame, level_nine_menu_adjective_button, level_nine_menu_noun_button, level_nine_menu_verb_button, level_nine_menu_verb2_button, level_nine_menu_noun2_button, level_ten_go_back_button, level_ten_generate_button, level_ten_story_label, level_ten_frame, level_ten_menu_noun_button, level_ten_menu_verb_button, level_ten_menu_verb2_button, level_ten_menu_verb3_button, level_ten_menu_noun2_button))
    level_button_3 = tk.Button(frame, text="level 3".upper(), width=25, height=5, pady=10, background='#5D6064', font=("Bauhaus 93", 16), fg='#CAF1DE', command=lambda: level_three(level_button_1, level_button_2, level_button_3, level_button_4, level_button_5, level_button_6, level_button_7, level_button_8, level_button_9, level_button_10, canvas, frame, go_back_button_2, scroll_bar, adventure_button, go_back_button, l, start_button, generate_level_one_button, go_back_button_level_one, label_story, level_one_frame, level_two_generate_button, level_two_go_back_button, label_story_level_two, level_two_frame, level_three_menu_adjective_button, level_three_menu_adjective2_button, level_three_menu_noun_button, level_three_menu_noun2_button, level_three_menu_verb_button, level_three_frame, level_four_generate_button, level_four_go_back_button, level_four_story_label, level_four_menu_adjective_button, level_four_menu_noun_button, level_four_menu_verb_button, level_four_menu_noun2_button, level_four_menu_noun3_button, level_four_frame, level_five_generate_button, level_five_go_back_button, level_five_story_label, level_five_frame, level_five_menu_adjective_button, level_five_menu_noun_button, level_five_menu_adverb_button, level_five_menu_verb_button, level_six_go_back_button, level_six_generate_button, level_six_story_label, level_six_frame, level_six_menu_adjective_button, level_six_menu_noun_button, level_six_menu_verb_button, level_six_menu_adjective2_button, level_six_menu_noun2_button, level_six_menu_noun3_button, level_seven_menu_adjective_button, level_seven_menu_noun_button, level_seven_menu_adjective2_button, level_seven_menu_verb_button, level_seven_menu_adjective3_button, level_seven_menu_noun2_button, level_seven_go_back_button, level_seven_generate_button, level_seven_story_label, level_seven_frame, level_eight_go_back_button, level_eight_generate_button, level_eight_story_label, level_eight_frame, level_eight_menu_noun_button, level_eight_menu_adjective_button, level_eight_menu_noun2_button, level_eight_menu_verb_button, level_eight_menu_noun3_button, level_eight_menu_verb2_button, level_eight_menu_adjective2_button, level_eight_menu_noun4_button, level_nine_go_back_button, level_nine_generate_button, level_nine_story_label, level_nine_frame, level_nine_menu_adjective_button, level_nine_menu_noun_button, level_nine_menu_verb_button, level_nine_menu_verb2_button, level_nine_menu_noun2_button, level_ten_go_back_button, level_ten_generate_button, level_ten_story_label, level_ten_frame, level_ten_menu_noun_button, level_ten_menu_verb_button, level_ten_menu_verb2_button, level_ten_menu_verb3_button, level_ten_menu_noun2_button))
    level_button_4 = tk.Button(frame, text="level 4".upper(), width=25, height=5, pady=10, background='#5D6064', font=("Bauhaus 93", 16), fg='#CAF1DE', command=lambda: level_four(level_button_1, level_button_2, level_button_3, level_button_4, level_button_5, level_button_6, level_button_7, level_button_8, level_button_9, level_button_10, canvas, scroll_bar, frame, go_back_button_2, adventure_button, go_back_button, l, start_button, generate_level_one_button, go_back_button_level_one, label_story, level_one_frame, level_two_generate_button, level_two_go_back_button, label_story_level_two, level_two_frame, level_three_generate_button, level_three_go_back_button, level_three_label_story, level_four_menu_adjective_button, level_four_menu_noun_button, level_four_menu_verb_button, level_four_menu_noun2_button, level_four_menu_noun3_button, level_three_frame, level_three_menu_adjective_button, level_three_menu_adjective2_button, level_three_menu_noun_button, level_three_menu_noun2_button, level_three_menu_verb_button, level_five_generate_button, level_five_go_back_button, level_five_story_label, level_five_frame, level_five_menu_adjective_button, level_five_menu_noun_button, level_five_menu_adverb_button, level_five_menu_verb_button, level_six_go_back_button, level_six_generate_button, level_six_story_label, level_six_frame, level_six_menu_adjective_button, level_six_menu_noun_button, level_six_menu_verb_button, level_six_menu_adjective2_button, level_six_menu_noun2_button, level_six_menu_noun3_button, level_seven_menu_adjective_button, level_seven_menu_noun_button, level_seven_menu_adjective2_button, level_seven_menu_verb_button, level_seven_menu_adjective3_button, level_seven_menu_noun2_button, level_seven_go_back_button, level_seven_generate_button, level_seven_story_label, level_seven_frame, level_eight_go_back_button, level_eight_generate_button, level_eight_story_label, level_eight_frame, level_eight_menu_noun_button, level_eight_menu_adjective_button, level_eight_menu_noun2_button, level_eight_menu_verb_button, level_eight_menu_noun3_button, level_eight_menu_verb2_button, level_eight_menu_adjective2_button, level_eight_menu_noun4_button, level_nine_go_back_button, level_nine_generate_button, level_nine_story_label, level_nine_frame, level_nine_menu_adjective_button, level_nine_menu_noun_button, level_nine_menu_verb_button, level_nine_menu_verb2_button, level_nine_menu_noun2_button, level_ten_go_back_button, level_ten_generate_button, level_ten_story_label, level_ten_frame, level_ten_menu_noun_button, level_ten_menu_verb_button, level_ten_menu_verb2_button, level_ten_menu_verb3_button, level_ten_menu_noun2_button))
    level_button_5 = tk.Button(frame, text="level 5".upper(), width=25, height=5, pady=10, background='#5D6064', font=('Bauhaus 93', 16), fg='#CAF1DE', command=lambda: level_five(level_button_1, level_button_2, level_button_3, level_button_4, level_button_5, level_button_6, level_button_7, level_button_8, level_button_9, level_button_10, canvas, scroll_bar, frame, go_back_button_2, adventure_button, go_back_button, l, start_button, generate_level_one_button, go_back_button_level_one, label_story, level_one_frame, level_two_generate_button, level_two_go_back_button, label_story_level_two, level_two_frame, level_three_generate_button, level_three_go_back_button, level_three_label_story, level_three_frame, level_four_generate_button, level_four_go_back_button, level_four_story_label, level_four_menu_adjective_button, level_four_menu_noun_button, level_four_menu_verb_button, level_four_menu_noun2_button, level_four_menu_noun3_button, level_four_frame, level_five_generate_button, level_five_go_back_button, level_five_story_label, level_five_frame, level_five_menu_adjective_button, level_five_menu_noun_button, level_five_menu_adverb_button, level_five_menu_verb_button, level_three_menu_adjective_button, level_three_menu_adjective2_button, level_three_menu_noun_button, level_three_menu_noun2_button, level_three_menu_verb_button, level_six_go_back_button, level_six_generate_button, level_six_story_label, level_six_frame, level_six_menu_adjective_button, level_six_menu_noun_button, level_six_menu_verb_button, level_six_menu_adjective2_button, level_six_menu_noun2_button, level_six_menu_noun3_button, level_seven_menu_adjective_button, level_seven_menu_noun_button, level_seven_menu_adjective2_button, level_seven_menu_verb_button, level_seven_menu_adjective3_button, level_seven_menu_noun2_button, level_seven_go_back_button, level_seven_generate_button, level_seven_story_label, level_seven_frame, level_eight_go_back_button, level_eight_generate_button, level_eight_story_label, level_eight_frame, level_eight_menu_noun_button, level_eight_menu_adjective_button, level_eight_menu_noun2_button, level_eight_menu_verb_button, level_eight_menu_noun3_button, level_eight_menu_verb2_button, level_eight_menu_adjective2_button, level_eight_menu_noun4_button, level_nine_go_back_button, level_nine_generate_button, level_nine_story_label, level_nine_frame, level_nine_menu_adjective_button, level_nine_menu_noun_button, level_nine_menu_verb_button, level_nine_menu_verb2_button, level_nine_menu_noun2_button, level_ten_go_back_button, level_ten_generate_button, level_ten_story_label, level_ten_frame, level_ten_menu_noun_button, level_ten_menu_verb_button, level_ten_menu_verb2_button, level_ten_menu_verb3_button, level_ten_menu_noun2_button))
    level_button_6 = tk.Button(frame, text="level 6".upper(), width=25, height=5, pady=10, background='#5D6064', font=("Bauhaus 93", 16), fg='#CAF1DE', command=lambda: level_six(level_button_1, level_button_2, level_button_3, level_button_4, level_button_5, level_button_6, level_button_7, level_button_8, level_button_9, level_button_10, canvas, scroll_bar, go_back_button_2, frame, adventure_button, go_back_button, l, start_button, generate_level_one_button, go_back_button_level_one, label_story, level_one_frame, level_two_generate_button, level_two_go_back_button, label_story_level_two, level_two_frame, level_three_generate_button, level_three_go_back_button, level_three_label_story, level_three_menu_adjective_button, level_three_menu_adjective2_button, level_three_menu_noun_button, level_three_menu_noun2_button, level_three_menu_verb_button, level_three_frame, level_four_generate_button, level_four_go_back_button, level_four_story_label, level_four_menu_adjective_button, level_four_menu_noun_button, level_four_menu_verb_button, level_four_menu_noun2_button, level_four_menu_noun3_button, level_four_frame, level_five_generate_button, level_five_go_back_button, level_five_story_label, level_five_frame, level_five_menu_adjective_button, level_five_menu_noun_button, level_five_menu_adverb_button, level_five_menu_verb_button, level_six_menu_adjective_button, level_six_menu_noun_button, level_six_menu_verb_button, level_six_menu_adjective2_button, level_six_menu_noun2_button, level_six_menu_noun3_button, level_seven_menu_adjective_button, level_seven_menu_noun_button, level_seven_menu_adjective2_button, level_seven_menu_verb_button, level_seven_menu_adjective3_button, level_seven_menu_noun2_button, level_seven_go_back_button, level_seven_generate_button, level_seven_story_label, level_seven_frame, level_eight_go_back_button, level_eight_generate_button, level_eight_story_label, level_eight_frame, level_eight_menu_noun_button, level_eight_menu_adjective_button, level_eight_menu_noun2_button, level_eight_menu_verb_button, level_eight_menu_noun3_button, level_eight_menu_verb2_button, level_eight_menu_adjective2_button, level_eight_menu_noun4_button, level_nine_go_back_button, level_nine_generate_button, level_nine_story_label, level_nine_frame, level_nine_menu_adjective_button, level_nine_menu_noun_button, level_nine_menu_verb_button, level_nine_menu_verb2_button, level_nine_menu_noun2_button, level_ten_go_back_button, level_ten_generate_button, level_ten_story_label, level_ten_frame, level_ten_menu_noun_button, level_ten_menu_verb_button, level_ten_menu_verb2_button, level_ten_menu_verb3_button, level_ten_menu_noun2_button))
    level_button_7 = tk.Button(frame, text="level 7".upper(), width=25, height=5, pady=10, background='#5D6064', font=("Bauhaus 93", 16), fg='#CAF1DE', command=lambda: level_seven(level_button_1, level_button_2, level_button_3, level_button_4, level_button_5, level_button_6, level_button_7, level_button_8, level_button_9, level_button_10, canvas, scroll_bar, go_back_button_2, frame, adventure_button, go_back_button, l, start_button, generate_level_one_button, go_back_button_level_one, label_story, level_one_frame, level_two_generate_button, level_two_go_back_button, label_story_level_two, level_two_frame, level_three_generate_button, level_three_go_back_button, level_three_label_story, level_three_menu_adjective_button, level_three_menu_adjective2_button, level_three_menu_noun_button, level_three_menu_noun2_button, level_three_menu_verb_button, level_three_frame, level_four_generate_button, level_four_go_back_button, level_four_story_label, level_four_menu_adjective_button, level_four_menu_noun_button, level_four_menu_verb_button, level_four_menu_noun2_button, level_four_menu_noun3_button, level_four_frame, level_five_generate_button, level_five_go_back_button, level_five_story_label, level_five_frame, level_five_menu_adjective_button, level_five_menu_noun_button, level_five_menu_adverb_button, level_five_menu_verb_button, level_six_menu_adjective_button, level_six_menu_noun_button, level_six_menu_verb_button, level_six_menu_adjective2_button, level_six_menu_noun2_button, level_six_menu_noun3_button, level_seven_menu_adjective_button, level_seven_menu_noun_button, level_seven_menu_adjective2_button, level_seven_menu_verb_button, level_seven_menu_adjective3_button, level_seven_menu_noun2_button, level_six_go_back_button, level_six_generate_button, level_six_story_label, level_six_frame, level_eight_go_back_button, level_eight_generate_button, level_eight_story_label, level_eight_frame, level_eight_menu_noun_button, level_eight_menu_adjective_button, level_eight_menu_noun2_button, level_eight_menu_verb_button, level_eight_menu_noun3_button, level_eight_menu_verb2_button, level_eight_menu_adjective2_button, level_eight_menu_noun4_button, level_nine_go_back_button, level_nine_generate_button, level_nine_story_label, level_nine_frame, level_nine_menu_adjective_button, level_nine_menu_noun_button, level_nine_menu_verb_button, level_nine_menu_verb2_button, level_nine_menu_noun2_button, level_ten_go_back_button, level_ten_generate_button, level_ten_story_label, level_ten_frame, level_ten_menu_noun_button, level_ten_menu_verb_button, level_ten_menu_verb2_button, level_ten_menu_verb3_button, level_ten_menu_noun2_button))
    level_button_8 = tk.Button(frame, text="level 8".upper(), width=25, height=5, pady=10, background='#5D6064', font=("Bauhaus 93", 16), fg='#CAF1DE', command=lambda: level_eight(level_button_1, level_button_2, level_button_3, level_button_4, level_button_5, level_button_6, level_button_7, level_button_8, level_button_9, level_button_10, canvas, scroll_bar, go_back_button_2, frame, adventure_button, go_back_button, l, start_button, generate_level_one_button, go_back_button_level_one, label_story, level_one_frame, level_two_generate_button, level_two_go_back_button, label_story_level_two, level_two_frame, level_three_generate_button, level_three_go_back_button, level_three_label_story, level_three_menu_adjective_button, level_three_menu_adjective2_button, level_three_menu_noun_button, level_three_menu_noun2_button, level_three_menu_verb_button, level_three_frame, level_four_generate_button, level_four_go_back_button, level_four_story_label, level_four_menu_adjective_button, level_four_menu_noun_button, level_four_menu_verb_button, level_four_menu_noun2_button, level_four_menu_noun3_button, level_four_frame, level_five_generate_button, level_five_go_back_button, level_five_story_label, level_five_frame, level_five_menu_adjective_button, level_five_menu_noun_button, level_five_menu_adverb_button, level_five_menu_verb_button, level_six_menu_adjective_button, level_six_menu_noun_button, level_six_menu_verb_button, level_six_menu_adjective2_button, level_six_menu_noun2_button, level_six_menu_noun3_button, level_seven_menu_adjective_button, level_seven_menu_noun_button, level_seven_menu_adjective2_button, level_seven_menu_verb_button, level_seven_menu_adjective3_button, level_seven_menu_noun2_button, level_six_go_back_button, level_six_generate_button, level_six_story_label, level_six_frame, level_eight_menu_noun_button, level_eight_menu_adjective_button, level_eight_menu_noun2_button, level_eight_menu_verb_button, level_eight_menu_noun3_button, level_eight_menu_verb2_button, level_eight_menu_adjective2_button, level_eight_menu_noun4_button, level_seven_go_back_button, level_seven_generate_button, level_seven_story_label, level_seven_frame, level_nine_go_back_button, level_nine_generate_button, level_nine_story_label, level_nine_frame, level_nine_menu_adjective_button, level_nine_menu_noun_button, level_nine_menu_verb_button, level_nine_menu_verb2_button, level_nine_menu_noun2_button, level_ten_go_back_button, level_ten_generate_button, level_ten_story_label, level_ten_frame, level_ten_menu_noun_button, level_ten_menu_verb_button, level_ten_menu_verb2_button, level_ten_menu_verb3_button, level_ten_menu_noun2_button))
    level_button_9 = tk.Button(frame, text="level 9".upper(), width=25, height=5, pady=10, background='#5D6064', font=("Bauhaus 93", 16), fg='#CAF1DE', command=lambda: level_nine(level_button_1, level_button_2, level_button_3, level_button_4, level_button_5, level_button_6, level_button_7, level_button_8, level_button_9, level_button_10, canvas, scroll_bar, go_back_button_2, frame, adventure_button, go_back_button, l, start_button, generate_level_one_button, go_back_button_level_one, label_story, level_one_frame, level_two_generate_button, level_two_go_back_button, label_story_level_two, level_two_frame, level_three_generate_button, level_three_go_back_button, level_three_label_story, level_three_menu_adjective_button, level_three_menu_adjective2_button, level_three_menu_noun_button, level_three_menu_noun2_button, level_three_menu_verb_button, level_three_frame, level_four_generate_button, level_four_go_back_button, level_four_story_label, level_four_menu_adjective_button, level_four_menu_noun_button, level_four_menu_verb_button, level_four_menu_noun2_button, level_four_menu_noun3_button, level_four_frame, level_five_generate_button, level_five_go_back_button, level_five_story_label, level_five_frame, level_five_menu_adjective_button, level_five_menu_noun_button, level_five_menu_adverb_button, level_five_menu_verb_button, level_six_menu_adjective_button, level_six_menu_noun_button, level_six_menu_verb_button, level_six_menu_adjective2_button, level_six_menu_noun2_button, level_six_menu_noun3_button, level_seven_menu_adjective_button, level_seven_menu_noun_button, level_seven_menu_adjective2_button, level_seven_menu_verb_button, level_seven_menu_adjective3_button, level_seven_menu_noun2_button, level_six_go_back_button, level_six_generate_button, level_six_story_label, level_six_frame, level_eight_menu_noun_button, level_eight_menu_adjective_button, level_eight_menu_noun2_button, level_eight_menu_verb_button, level_eight_menu_noun3_button, level_eight_menu_verb2_button, level_eight_menu_adjective2_button, level_eight_menu_noun4_button, level_seven_go_back_button, level_seven_generate_button, level_seven_story_label, level_seven_frame, level_nine_go_back_button, level_nine_generate_button, level_nine_story_label, level_nine_frame, level_nine_menu_adjective_button, level_nine_menu_noun_button, level_nine_menu_verb_button, level_nine_menu_verb2_button, level_nine_menu_noun2_button, level_eight_go_back_button, level_eight_generate_button, level_eight_story_label, level_eight_frame, level_ten_go_back_button, level_ten_generate_button, level_ten_story_label, level_ten_frame, level_ten_menu_noun_button, level_ten_menu_verb_button, level_ten_menu_verb2_button, level_ten_menu_verb3_button, level_ten_menu_noun2_button))
    level_button_10 = tk.Button(frame, text="level 10".upper(), width=25, height=5, pady=10, background='#5D6064', font=("Bauhaus 93", 16), fg='#CAF1DE', command=lambda: level_ten(level_button_1, level_button_2, level_button_3, level_button_4, level_button_5, level_button_6, level_button_7, level_button_8, level_button_9, level_button_10, canvas, scroll_bar, go_back_button_2, frame, adventure_button, go_back_button, l, start_button, generate_level_one_button, go_back_button_level_one, label_story, level_one_frame, level_two_generate_button, level_two_go_back_button, label_story_level_two, level_two_frame, level_three_generate_button, level_three_go_back_button, level_three_label_story, level_three_menu_adjective_button, level_three_menu_adjective2_button, level_three_menu_noun_button, level_three_menu_noun2_button, level_three_menu_verb_button, level_three_frame, level_four_generate_button, level_four_go_back_button, level_four_story_label, level_four_menu_adjective_button, level_four_menu_noun_button, level_four_menu_verb_button, level_four_menu_noun2_button, level_four_menu_noun3_button, level_four_frame, level_five_generate_button, level_five_go_back_button, level_five_story_label, level_five_frame, level_five_menu_adjective_button, level_five_menu_noun_button, level_five_menu_adverb_button, level_five_menu_verb_button, level_six_menu_adjective_button, level_six_menu_noun_button, level_six_menu_verb_button, level_six_menu_adjective2_button, level_six_menu_noun2_button, level_six_menu_noun3_button, level_seven_menu_adjective_button, level_seven_menu_noun_button, level_seven_menu_adjective2_button, level_seven_menu_verb_button, level_seven_menu_adjective3_button, level_seven_menu_noun2_button, level_six_go_back_button, level_six_generate_button, level_six_story_label, level_six_frame, level_eight_menu_noun_button, level_eight_menu_adjective_button, level_eight_menu_noun2_button, level_eight_menu_verb_button, level_eight_menu_noun3_button, level_eight_menu_verb2_button, level_eight_menu_adjective2_button, level_eight_menu_noun4_button, level_seven_go_back_button, level_seven_generate_button, level_seven_story_label, level_seven_frame, level_nine_go_back_button, level_nine_generate_button, level_nine_story_label, level_nine_frame, level_nine_menu_adjective_button, level_nine_menu_noun_button, level_nine_menu_verb_button, level_nine_menu_verb2_button, level_nine_menu_noun2_button, level_eight_go_back_button, level_eight_generate_button, level_eight_story_label, level_eight_frame, level_ten_menu_noun_button, level_ten_menu_verb_button, level_ten_menu_verb2_button, level_ten_menu_verb3_button, level_ten_menu_noun2_button))

    level_button_1.pack()
    level_button_2.pack()
    level_button_3.pack()
    level_button_4.pack()
    level_button_5.pack()
    level_button_6.pack()
    level_button_7.pack()
    level_button_8.pack()
    level_button_9.pack()
    level_button_10.pack()

    frame.update_idletasks()
    canvas.configure(scrollregion=canvas.bbox('all'))

    if adventure_button:
        adventure_button.pack_forget()
        go_back_button.pack_forget()

    # level one 
    if go_back_button_level_one: 
        generate_level_one_button.pack_forget()
        go_back_button_level_one.pack_forget()
        label_story.pack_forget()
        menu_noun_button.pack_forget()
        menu_noun2_button.pack_forget()
        menu_verb_button.pack_forget()
        menu_adj_button.pack_forget()
        level_one_frame.pack_forget()

    # level two
    if level_two_go_back_button: 
        level_two_generate_button.pack_forget()
        level_two_go_back_button.pack_forget()
        label_story_level_two.pack_forget()
        level_two_menu_adj_button.pack_forget()
        level_two_menu_adj2_button.pack_forget()
        level_two_menu_noun_button.pack_forget()
        level_two_menu_verb_button.pack_forget()
        level_two_frame.pack_forget()

    # level three
    if level_three_go_back_button: 
        level_three_generate_button.pack_forget()
        level_three_go_back_button.pack_forget()
        level_three_label_story.pack_forget()
        level_three_frame.pack_forget()
        level_three_menu_adjective_button.pack_forget()
        level_three_menu_noun_button.pack_forget()
        level_three_menu_adjective2_button.pack_forget()
        level_three_menu_verb_button.pack_forget()
        level_three_menu_noun2_button.pack_forget()

    # level four
    if level_four_go_back_button: 
        level_four_generate_button.pack_forget()
        level_four_go_back_button.pack_forget()
        level_four_story_label.pack_forget()
        level_four_frame.pack_forget()
        level_four_menu_adjective_button.pack_forget()
        level_four_menu_noun_button.pack_forget()
        level_four_menu_verb_button.pack_forget()
        level_four_menu_noun2_button.pack_forget()
        level_four_menu_noun3_button.pack_forget()

    # level five
    if level_five_go_back_button: 
        level_five_generate_button.pack_forget()
        level_five_go_back_button.pack_forget()
        level_five_story_label.pack_forget()
        level_five_frame.pack_forget()
        level_five_menu_adjective_button.pack_forget()
        level_five_menu_noun_button.pack_forget()
        level_five_menu_adverb_button.pack_forget()
        level_five_menu_verb_button.pack_forget()

    # level six
    if level_six_go_back_button: 
        level_six_generate_button.pack_forget()
        level_six_go_back_button.pack_forget()
        level_six_story_label.pack_forget()
        level_six_frame.pack_forget()
        level_six_menu_adjective_button.pack_forget()
        level_six_menu_noun_button.pack_forget()
        level_six_menu_verb_button.pack_forget()
        level_six_menu_adjective2_button.pack_forget()
        level_six_menu_noun2_button.pack_forget()
        level_six_menu_noun3_button.pack_forget()     

    # level seven
    if level_seven_go_back_button: 
        level_seven_generate_button.pack_forget()
        level_seven_go_back_button.pack_forget()
        level_seven_story_label.pack_forget()
        level_seven_frame.pack_forget()
        level_seven_menu_adjective_button.pack_forget()
        level_seven_menu_noun_button.pack_forget()
        level_seven_menu_adjective2_button.pack_forget()
        level_seven_menu_verb_button.pack_forget()
        level_seven_menu_adjective3_button.pack_forget()
        level_seven_menu_noun2_button.pack_forget()  

    # level eight
    if level_eight_go_back_button: 
        level_eight_generate_button.pack_forget()
        level_eight_go_back_button.pack_forget()
        level_eight_story_label.pack_forget()
        level_eight_frame.pack_forget()
        level_eight_menu_noun_button.pack_forget()
        level_eight_menu_adjective_button.pack_forget()
        level_eight_menu_noun2_button.pack_forget()
        level_eight_menu_verb_button.pack_forget()
        level_eight_menu_noun3_button.pack_forget()
        level_eight_menu_verb2_button.pack_forget()
        level_eight_menu_adjective2_button.pack_forget()
        level_eight_menu_noun4_button.pack_forget() 

    # level nine
    if level_nine_go_back_button: 
        level_nine_generate_button.pack_forget()
        level_nine_go_back_button.pack_forget()
        level_nine_story_label.pack_forget()
        level_nine_frame.pack_forget()
        level_nine_menu_adjective_button.pack_forget()
        level_nine_menu_noun_button.pack_forget()
        level_nine_menu_verb_button.pack_forget()
        level_nine_menu_verb2_button.pack_forget()
        level_nine_menu_noun2_button.pack_forget()

    # level ten
    if level_ten_go_back_button: 
        level_ten_generate_button.pack_forget()
        level_ten_go_back_button.pack_forget()
        level_ten_story_label.pack_forget()
        level_ten_frame.pack_forget()
        level_ten_menu_noun_button.pack_forget()
        level_ten_menu_verb_button.pack_forget()
        level_ten_menu_verb2_button.pack_forget()
        level_ten_menu_noun_button.pack_forget()
        level_ten_menu_verb3_button.pack_forget()
        level_ten_menu_noun2_button.pack_forget()

# setup
root = tk.Tk()

root.geometry("500x500")
root.title("WordFiller")
root.resizable(0, 0)
root.configure(background='#35393e')
root.after(0, start_screen, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None)

root.mainloop()