import os
import time
import wx
import sys

from wx.core import Size

class ProgramFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title="Cota Modificada", 
                        size=(1000,670), style= wx.MINIMIZE_BOX | wx.SYSTEM_MENU |
                         wx.CAPTION | wx.CLOSE_BOX | wx.CLIP_CHILDREN)
        # Set BackGroud Color
        self.SetBackgroundColour("WHITE")
        
        # Add the menu
        self.creat_menu()

        # Add the main Panel
        self.panel = ProgramPanel(self)

        self.Centre()
        self.Show()

    # Create the menu
    def creat_menu(self):
        menu_bar = wx.MenuBar()

        # Add the Ficheiro Part to the menu
        ficheiro_menu = wx.Menu()

        new_menu_item = ficheiro_menu.Append(wx.ID_ANY, "Novo")
        self.Bind(
            event=wx.EVT_MENU,
            handler=self.on_new_menu_item,
            source=new_menu_item
        )

        sair_menu_item = ficheiro_menu.Append(wx.ID_ANY, "Sair")
        self.Bind(
            event=wx.EVT_MENU,
            handler=self.on_sair_menu_item,
            source=sair_menu_item
        )
        menu_bar.Append(ficheiro_menu, "Ficheiro")

        self.SetMenuBar(menu_bar)

    # When novo button is pressed
    def on_new_menu_item(self, event):
        print('hello world')
        # TODO

    # When sair button is pressed
    def on_sair_menu_item(self, event):
        self.Destroy()

class ProgramPanel(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)

        # Fonts
        font_A = wx.Font(15, wx.MODERN, wx.NORMAL, wx.NORMAL, False, u'Consolas')
        font_B = wx.Font(20, wx.MODERN, wx.NORMAL, wx.NORMAL, False, u'Consolas')


        # Add Labeling Items
        label_Valores = wx.StaticText(
            self, label='Valores',
            pos=(80,10), size=(50,35), style= wx.ALIGN_LEFT
        )
        label_Valores.SetFont(font_B)


        label_quotaPadrao = wx.StaticText(
            self, label='Padrao',
            pos=(300,10), size=(50,35), style= wx.ALIGN_LEFT
        )
        label_quotaPadrao.SetFont(font_B)


        label_quotaPadraoArredondada = wx.StaticText(
            self, label='Arr.',
            pos=(450,10), size=(50,35), style= wx.ALIGN_LEFT
        )
        label_quotaPadraoArredondada.SetFont(font_B)


        label_quotaModificada = wx.StaticText(
            self, label='Modificada',
            pos=(650,10), size=(50,35), style= wx.ALIGN_LEFT
        )
        label_quotaModificada.SetFont(font_B)


        label_quotaModificadaArredondada = wx.StaticText(
            self, label='Arr.',
            pos=(850,10), size=(50,35), style= wx.ALIGN_LEFT
        )
        label_quotaModificadaArredondada.SetFont(font_B)


        # Add Values Items
        #1.1
        label_A = wx.StaticText(
            self, label='A:',
            pos=(10,50), size=(10,20), style= wx.ALIGN_LEFT
        )
        label_A.SetFont(font_A)

        #1.2
        self.textBox_A = wx.TextCtrl(
            self, value='',
            pos=(40,49), size=(200,27), 
            style=wx.TE_RICH | wx.TE_PROCESS_ENTER
        )
        self.textBox_A.SetFont(font_A)
        self.Bind(
            event=wx.EVT_TEXT,
            handler=self.numberEnterHandler,
            source=self.textBox_A
        )

        #1.3
        self.label_quotaPadrao_A = wx.StaticText(
            self, label='21',
            pos=(250,50), size=(180,20), style= wx.ALIGN_CENTER
        )
        self.label_quotaPadrao_A.SetFont(font_A)

        #1.4
        self.label_quotaPadraoArredondada_A = wx.StaticText(
            self, label='22',
            pos=(450,50), size=(40,20), style= wx.ALIGN_CENTER
        )
        self.label_quotaPadraoArredondada_A.SetFont(font_A)

        #1.5
        self.label_quotaModificada_A = wx.StaticText(
            self, label='23',
            pos=(635,50), size=(180,20), style= wx.ALIGN_CENTER
        )
        self.label_quotaModificada_A.SetFont(font_A)

        #1.6
        self.label_quotaModificadaArredondada_A = wx.StaticText(
            self, label='24',
            pos=(852,50), size=(40,20), style= wx.ALIGN_CENTER
        )
        self.label_quotaModificadaArredondada_A.SetFont(font_A)


        #2.1
        label_B = wx.StaticText(
            self, label='B:',
            pos=(10,90), size=(10,20), style= wx.ALIGN_LEFT
        )
        label_B.SetFont(font_A)

        #2.2
        self.textBox_B = wx.TextCtrl(
            self, value='',
            pos=(40,90), size=(200,27), 
            style=wx.TE_RICH | wx.TE_PROCESS_ENTER
        )
        self.textBox_B.SetFont(font_A)
        self.Bind(
            event=wx.EVT_TEXT,
            handler=self.numberEnterHandler,
            source=self.textBox_B
        )

        #2.3
        self.label_quotaPadrao_B = wx.StaticText(
            self, label='21',
            pos=(250,90), size=(180,20), style= wx.ALIGN_CENTER
        )
        self.label_quotaPadrao_B.SetFont(font_A)

        #2.4
        self.label_quotaPadraoArredondada_B = wx.StaticText(
            self, label='22',
            pos=(450,90), size=(40,20), style= wx.ALIGN_CENTER
        )
        self.label_quotaPadraoArredondada_B.SetFont(font_A)

        #2.5
        self.label_quotaModificada_B = wx.StaticText(
            self, label='23',
            pos=(635,90), size=(180,20), style= wx.ALIGN_CENTER
        )
        self.label_quotaModificada_B.SetFont(font_A)

        #2.6
        self.label_quotaModificadaArredondada_B = wx.StaticText(
            self, label='24',
            pos=(852,90), size=(40,20), style= wx.ALIGN_CENTER
        )
        self.label_quotaModificadaArredondada_B.SetFont(font_A)


        #3.1
        label_C = wx.StaticText(
            self, label='C:',
            pos=(10,130), size=(10,20), style= wx.ALIGN_LEFT
        )
        label_C.SetFont(font_A)

        #3.2
        self.textBox_C = wx.TextCtrl(
            self, value='',
            pos=(40,130), size=(200,27), 
            style=wx.TE_RICH | wx.TE_PROCESS_ENTER
        )
        self.textBox_C.SetFont(font_A)
        self.Bind(
            event=wx.EVT_TEXT,
            handler=self.numberEnterHandler,
            source=self.textBox_C
        )

        #3.3
        self.label_quotaPadrao_C = wx.StaticText(
            self, label='21',
            pos=(250,130), size=(180,20), style= wx.ALIGN_CENTER
        )
        self.label_quotaPadrao_C.SetFont(font_A)

        #3.4
        self.label_quotaPadraoArredondada_C = wx.StaticText(
            self, label='22',
            pos=(450,130), size=(40,20), style= wx.ALIGN_CENTER
        )
        self.label_quotaPadraoArredondada_C.SetFont(font_A)

        #3.5
        self.label_quotaModificada_C = wx.StaticText(
            self, label='23',
            pos=(635,130), size=(180,20), style= wx.ALIGN_CENTER
        )
        self.label_quotaModificada_C.SetFont(font_A)

        #3.6
        self.label_quotaModificadaArredondada_C = wx.StaticText(
            self, label='24',
            pos=(852,130), size=(40,20), style= wx.ALIGN_CENTER
        )
        self.label_quotaModificadaArredondada_C.SetFont(font_A)


        #4.1
        label_D = wx.StaticText(
            self, label='D:',
            pos=(10,170), size=(10,20), style= wx.ALIGN_LEFT
        )
        label_D.SetFont(font_A)

        #4.2
        self.textBox_D = wx.TextCtrl(
            self, value='',
            pos=(40,170), size=(200,27), 
            style=wx.TE_RICH | wx.TE_PROCESS_ENTER
        )
        self.textBox_D.SetFont(font_A)
        self.Bind(
            event=wx.EVT_TEXT,
            handler=self.numberEnterHandler,
            source=self.textBox_D
        )

        #4.3
        self.label_quotaPadrao_D = wx.StaticText(
            self, label='21',
            pos=(250,170), size=(180,20), style= wx.ALIGN_CENTER
        )
        self.label_quotaPadrao_D.SetFont(font_A)

        #4.4
        self.label_quotaPadraoArredondada_D = wx.StaticText(
            self, label='22',
            pos=(450,170), size=(40,20), style= wx.ALIGN_CENTER
        )
        self.label_quotaPadraoArredondada_D.SetFont(font_A)

        #4.5
        self.label_quotaModificada_D = wx.StaticText(
            self, label='23',
            pos=(635,170), size=(180,20), style= wx.ALIGN_CENTER
        )
        self.label_quotaModificada_D.SetFont(font_A)

        #4.6
        self.label_quotaModificadaArredondada_D = wx.StaticText(
            self, label='24',
            pos=(852,170), size=(40,20), style= wx.ALIGN_CENTER
        )
        self.label_quotaModificadaArredondada_D.SetFont(font_A)


        #5.1
        label_E = wx.StaticText(
            self, label='E:',
            pos=(10,210), size=(10,20), style= wx.ALIGN_LEFT
        )
        label_E.SetFont(font_A)

        #5.2
        self.textBox_E = wx.TextCtrl(
            self, value='',
            pos=(40,210),size=(200,27), 
            style=wx.TE_RICH | wx.TE_PROCESS_ENTER
        )
        self.textBox_E.SetFont(font_A)
        self.Bind(
            event=wx.EVT_TEXT,
            handler=self.numberEnterHandler,
            source=self.textBox_E
        )

        #5.3
        self.label_quotaPadrao_E = wx.StaticText(
            self, label='21',
            pos=(250,210), size=(180,20), style= wx.ALIGN_CENTER
        )
        self.label_quotaPadrao_E.SetFont(font_A)

        #5.4
        self.label_quotaPadraoArredondada_E = wx.StaticText(
            self, label='22',
            pos=(450,210), size=(40,20), style= wx.ALIGN_CENTER
        )
        self.label_quotaPadraoArredondada_E.SetFont(font_A)

        #5.5
        self.label_quotaModificada_E = wx.StaticText(
            self, label='23',
            pos=(635,210), size=(180,20), style= wx.ALIGN_CENTER
        )
        self.label_quotaModificada_E.SetFont(font_A)

        #5.6
        self.label_quotaModificadaArredondada_E = wx.StaticText(
            self, label='24',
            pos=(852,210), size=(40,20), style= wx.ALIGN_CENTER
        )
        self.label_quotaModificadaArredondada_E.SetFont(font_A)


        #6.1
        label_F = wx.StaticText(
            self, label='F:',
            pos=(10,250), size=(10,20), style= wx.ALIGN_LEFT
        )
        label_F.SetFont(font_A)

        #6.2
        self.textBox_F = wx.TextCtrl(
            self, value='',
            pos=(40,250),size=(200,27), 
            style=wx.TE_RICH | wx.TE_PROCESS_ENTER
        )
        self.textBox_F.SetFont(font_A)
        self.Bind(
            event=wx.EVT_TEXT,
            handler=self.numberEnterHandler,
            source=self.textBox_F
        )

        #6.3
        self.label_quotaPadrao_F = wx.StaticText(
            self, label='21',
            pos=(250,250), size=(180,20), style= wx.ALIGN_CENTER
        )
        self.label_quotaPadrao_F.SetFont(font_A)

        #6.4
        self.label_quotaPadraoArredondada_F = wx.StaticText(
            self, label='22',
            pos=(450,250), size=(40,20), style= wx.ALIGN_CENTER
        )
        self.label_quotaPadraoArredondada_F.SetFont(font_A)

        #6.5
        self.label_quotaModificada_F = wx.StaticText(
            self, label='23',
            pos=(635,250), size=(180,20), style= wx.ALIGN_CENTER
        )
        self.label_quotaModificada_F.SetFont(font_A)

        #6.6
        self.label_quotaModificadaArredondada_F = wx.StaticText(
            self, label='24',
            pos=(852,250), size=(40,20), style= wx.ALIGN_CENTER
        )
        self.label_quotaModificadaArredondada_F.SetFont(font_A)


        #7.1
        label_G = wx.StaticText(
            self, label='G:',
            pos=(10,290), size=(10,20), style= wx.ALIGN_LEFT
        )
        label_G.SetFont(font_A)

        #7.2
        self.textBox_G = wx.TextCtrl(
            self, value='',
            pos=(40,290),size=(200,27), 
            style=wx.TE_RICH | wx.TE_PROCESS_ENTER
        )
        self.textBox_G.SetFont(font_A)
        self.Bind(
            event=wx.EVT_TEXT,
            handler=self.numberEnterHandler,
            source=self.textBox_G
        )

        #7.3
        self.label_quotaPadrao_G = wx.StaticText(
            self, label='21',
            pos=(250,290), size=(180,20), style= wx.ALIGN_CENTER
        )
        self.label_quotaPadrao_G.SetFont(font_A)

        #7.4
        self.label_quotaPadraoArredondada_G = wx.StaticText(
            self, label='22',
            pos=(450,290), size=(40,20), style= wx.ALIGN_CENTER
        )
        self.label_quotaPadraoArredondada_G.SetFont(font_A)

        #7.5
        self.label_quotaModificada_G = wx.StaticText(
            self, label='23',
            pos=(635,290), size=(180,20), style= wx.ALIGN_CENTER
        )
        self.label_quotaModificada_G.SetFont(font_A)

        #7.6
        self.label_quotaModificadaArredondada_G = wx.StaticText(
            self, label='24',
            pos=(852,290), size=(40,20), style= wx.ALIGN_CENTER
        )
        self.label_quotaModificadaArredondada_G.SetFont(font_A)


        #8.1
        label_H = wx.StaticText(
            self, label='H:',
            pos=(10,330), size=(10,20), style= wx.ALIGN_LEFT
        )
        label_H.SetFont(font_A)

        #8.2
        self.textBox_H = wx.TextCtrl(
            self, value='',
            pos=(40,330),size=(200,27), 
            style=wx.TE_RICH | wx.TE_PROCESS_ENTER
        )
        self.textBox_H.SetFont(font_A)
        self.Bind(
            event=wx.EVT_TEXT,
            handler=self.numberEnterHandler,
            source=self.textBox_H
        )

        #8.3
        self.label_quotaPadrao_H = wx.StaticText(
            self, label='21',
            pos=(250,330), size=(180,20), style= wx.ALIGN_CENTER
        )
        self.label_quotaPadrao_H.SetFont(font_A)

        #8.4
        self.label_quotaPadraoArredondada_H = wx.StaticText(
            self, label='22',
            pos=(450,330), size=(40,20), style= wx.ALIGN_CENTER
        )
        self.label_quotaPadraoArredondada_H.SetFont(font_A)

        #8.5
        self.label_quotaModificada_H = wx.StaticText(
            self, label='23',
            pos=(635,330), size=(180,20), style= wx.ALIGN_CENTER
        )
        self.label_quotaModificada_H.SetFont(font_A)

        #8.6
        self.label_quotaModificadaArredondada_H = wx.StaticText(
            self, label='24',
            pos=(852,330), size=(40,20), style= wx.ALIGN_CENTER
        )
        self.label_quotaModificadaArredondada_H.SetFont(font_A)


        #9.1
        label_I = wx.StaticText(
            self, label='I:',
            pos=(10,370), size=(10,20), style= wx.ALIGN_LEFT
        )
        label_I.SetFont(font_A)

        #9.2
        self.textBox_I = wx.TextCtrl(
            self, value='',
            pos=(40,370),size=(200,27), 
            style=wx.TE_RICH | wx.TE_PROCESS_ENTER
        )
        self.textBox_I.SetFont(font_A)
        self.Bind(
            event=wx.EVT_TEXT,
            handler=self.numberEnterHandler,
            source=self.textBox_I
        )

        #9.3
        self.label_quotaPadrao_I = wx.StaticText(
            self, label='21',
            pos=(250,370), size=(180,20), style= wx.ALIGN_CENTER
        )
        self.label_quotaPadrao_I.SetFont(font_A)

        #9.4
        self.label_quotaPadraoArredondada_I = wx.StaticText(
            self, label='22',
            pos=(450,370), size=(40,20), style= wx.ALIGN_CENTER
        )
        self.label_quotaPadraoArredondada_I.SetFont(font_A)

        #9.5
        self.label_quotaModificada_I = wx.StaticText(
            self, label='23',
            pos=(635,370), size=(180,20), style= wx.ALIGN_CENTER
        )
        self.label_quotaModificada_I.SetFont(font_A)

        #9.6
        self.label_quotaModificadaArredondada_I = wx.StaticText(
            self, label='24',
            pos=(852,370), size=(40,20), style= wx.ALIGN_CENTER
        )
        self.label_quotaModificadaArredondada_I.SetFont(font_A)


        #10.1
        label_J = wx.StaticText(
            self, label='J:',
            pos=(10,410), size=(10,20), style= wx.ALIGN_LEFT
        )
        label_J.SetFont(font_A)

        #10.2
        self.textBox_J = wx.TextCtrl(
            self, value='',
            pos=(40,410),size=(200,27), 
            style=wx.TE_RICH | wx.TE_PROCESS_ENTER
        )
        self.textBox_J.SetFont(font_A)
        self.Bind(
            event=wx.EVT_TEXT,
            handler=self.numberEnterHandler,
            source=self.textBox_J
        )

        #10.3
        self.label_quotaPadrao_J = wx.StaticText(
            self, label='21',
            pos=(250,410), size=(180,20), style= wx.ALIGN_CENTER
        )
        self.label_quotaPadrao_J.SetFont(font_A)

        #10.4
        self.label_quotaPadraoArredondada_J = wx.StaticText(
            self, label='22',
            pos=(450,410), size=(40,20), style= wx.ALIGN_CENTER
        )
        self.label_quotaPadraoArredondada_J.SetFont(font_A)

        #10.5
        self.label_quotaModificada_J = wx.StaticText(
            self, label='23',
            pos=(635,410), size=(180,20), style= wx.ALIGN_CENTER
        )
        self.label_quotaModificada_J.SetFont(font_A)

        #10.6
        self.label_quotaModificadaArredondada_J = wx.StaticText(
            self, label='24',
            pos=(852,410), size=(40,20), style= wx.ALIGN_CENTER
        )
        self.label_quotaModificadaArredondada_J.SetFont(font_A)


        #11.1
        label_K = wx.StaticText(
            self, label='K:',
            pos=(10,450), size=(10,20), style= wx.ALIGN_LEFT
        )
        label_K.SetFont(font_A)

        #11.2
        self.textBox_K = wx.TextCtrl(
            self, value='',
            pos=(40,450),size=(200,27), 
            style=wx.TE_RICH | wx.TE_PROCESS_ENTER
        )
        self.textBox_K.SetFont(font_A)
        self.Bind(
            event=wx.EVT_TEXT,
            handler=self.numberEnterHandler,
            source=self.textBox_K
        )

        #11.3
        self.label_quotaPadrao_K = wx.StaticText(
            self, label='21',
            pos=(250,450), size=(180,20), style= wx.ALIGN_CENTER
        )
        self.label_quotaPadrao_K.SetFont(font_A)

        #11.4
        self.label_quotaPadraoArredondada_K = wx.StaticText(
            self, label='22',
            pos=(450,450), size=(40,20), style= wx.ALIGN_CENTER
        )
        self.label_quotaPadraoArredondada_K.SetFont(font_A)

        #11.5
        self.label_quotaModificada_K = wx.StaticText(
            self, label='23',
            pos=(635,450), size=(180,20), style= wx.ALIGN_CENTER
        )
        self.label_quotaModificada_K.SetFont(font_A)

        #11.6
        self.label_quotaModificadaArredondada_K = wx.StaticText(
            self, label='24',
            pos=(852,450), size=(40,20), style= wx.ALIGN_CENTER
        )
        self.label_quotaModificadaArredondada_K.SetFont(font_A)


        #12.1
        label_L = wx.StaticText(
            self, label='L:',
            pos=(10,490), size=(10,20), style= wx.ALIGN_LEFT
        )
        label_L.SetFont(font_A)

        #12.2
        self.textBox_L = wx.TextCtrl(
            self, value='',
            pos=(40,490),size=(200,27), 
            style=wx.TE_RICH | wx.TE_PROCESS_ENTER
        )
        self.textBox_L.SetFont(font_A)
        self.Bind(
            event=wx.EVT_TEXT,
            handler=self.numberEnterHandler,
            source=self.textBox_L
        )

        #12.3
        self.label_quotaPadrao_L = wx.StaticText(
            self, label='21',
            pos=(250,490), size=(180,20), style= wx.ALIGN_CENTER
        )
        self.label_quotaPadrao_L.SetFont(font_A)

        #12.4
        self.label_quotaPadraoArredondada_L = wx.StaticText(
            self, label='22',
            pos=(450,490), size=(40,20), style= wx.ALIGN_CENTER
        )
        self.label_quotaPadraoArredondada_L.SetFont(font_A)

        #12.5
        self.label_quotaModificada_L = wx.StaticText(
            self, label='23',
            pos=(635,490), size=(180,20), style= wx.ALIGN_CENTER
        )
        self.label_quotaModificada_L.SetFont(font_A)

        #12.6
        self.label_quotaModificadaArredondada_L = wx.StaticText(
            self, label='24',
            pos=(852,490), size=(40,20), style= wx.ALIGN_CENTER
        )
        self.label_quotaModificadaArredondada_L.SetFont(font_A)


        #13.1
        label_M = wx.StaticText(
            self, label='M:',
            pos=(10,530), size=(10,20), style= wx.ALIGN_LEFT
        )
        label_M.SetFont(font_A)

        #13.2
        self.textBox_M = wx.TextCtrl(
            self, value='',
            pos=(40,530),size=(200,27), 
            style=wx.TE_RICH | wx.TE_PROCESS_ENTER
        )
        self.textBox_M.SetFont(font_A)
        self.Bind(
            event=wx.EVT_TEXT,
            handler=self.numberEnterHandler,
            source=self.textBox_M
        )

        #13.3
        self.label_quotaPadrao_M = wx.StaticText(
            self, label='21',
            pos=(250,530), size=(180,20), style= wx.ALIGN_CENTER
        )
        self.label_quotaPadrao_M.SetFont(font_A)

        #13.4
        self.label_quotaPadraoArredondada_M = wx.StaticText(
            self, label='22',
            pos=(450,530), size=(40,20), style= wx.ALIGN_CENTER
        )
        self.label_quotaPadraoArredondada_M.SetFont(font_A)

        #13.5
        self.label_quotaModificada_M = wx.StaticText(
            self, label='23',
            pos=(635,530), size=(180,20), style= wx.ALIGN_CENTER
        )
        self.label_quotaModificada_M.SetFont(font_A)

        #13.6
        self.label_quotaModificadaArredondada_M = wx.StaticText(
            self, label='24',
            pos=(852,530), size=(40,20), style= wx.ALIGN_CENTER
        )
        self.label_quotaModificadaArredondada_M.SetFont(font_A)


        # Color
        self.label_quotaPadrao_A.SetForegroundColour(wx.Colour(100,150,100))
        self.label_quotaPadrao_B.SetForegroundColour(wx.Colour(100,150,100))
        self.label_quotaPadrao_C.SetForegroundColour(wx.Colour(100,150,100))
        self.label_quotaPadrao_D.SetForegroundColour(wx.Colour(100,150,100))
        self.label_quotaPadrao_E.SetForegroundColour(wx.Colour(100,150,100))
        self.label_quotaPadrao_F.SetForegroundColour(wx.Colour(100,150,100))
        self.label_quotaPadrao_G.SetForegroundColour(wx.Colour(100,150,100))
        self.label_quotaPadrao_H.SetForegroundColour(wx.Colour(100,150,100))
        self.label_quotaPadrao_I.SetForegroundColour(wx.Colour(100,150,100))
        self.label_quotaPadrao_J.SetForegroundColour(wx.Colour(100,150,100))
        self.label_quotaPadrao_K.SetForegroundColour(wx.Colour(100,150,100))
        self.label_quotaPadrao_L.SetForegroundColour(wx.Colour(100,150,100))
        self.label_quotaPadrao_M.SetForegroundColour(wx.Colour(100,150,100))
        
        self.label_quotaPadraoArredondada_A.SetForegroundColour(wx.Colour(50,130,50))
        self.label_quotaPadraoArredondada_B.SetForegroundColour(wx.Colour(50,130,50))
        self.label_quotaPadraoArredondada_C.SetForegroundColour(wx.Colour(50,130,50))
        self.label_quotaPadraoArredondada_D.SetForegroundColour(wx.Colour(50,130,50))
        self.label_quotaPadraoArredondada_E.SetForegroundColour(wx.Colour(50,130,50))
        self.label_quotaPadraoArredondada_F.SetForegroundColour(wx.Colour(50,130,50))
        self.label_quotaPadraoArredondada_G.SetForegroundColour(wx.Colour(50,130,50))
        self.label_quotaPadraoArredondada_H.SetForegroundColour(wx.Colour(50,130,50))
        self.label_quotaPadraoArredondada_I.SetForegroundColour(wx.Colour(50,130,50))
        self.label_quotaPadraoArredondada_J.SetForegroundColour(wx.Colour(50,130,50))
        self.label_quotaPadraoArredondada_K.SetForegroundColour(wx.Colour(50,130,50))
        self.label_quotaPadraoArredondada_L.SetForegroundColour(wx.Colour(50,130,50))
        self.label_quotaPadraoArredondada_M.SetForegroundColour(wx.Colour(50,130,50))

        self.label_quotaModificada_A.SetForegroundColour(wx.Colour(60,60,160))
        self.label_quotaModificada_B.SetForegroundColour(wx.Colour(60,60,160))
        self.label_quotaModificada_C.SetForegroundColour(wx.Colour(60,60,160))
        self.label_quotaModificada_D.SetForegroundColour(wx.Colour(60,60,160))
        self.label_quotaModificada_E.SetForegroundColour(wx.Colour(60,60,160))
        self.label_quotaModificada_F.SetForegroundColour(wx.Colour(60,60,160))
        self.label_quotaModificada_G.SetForegroundColour(wx.Colour(60,60,160))
        self.label_quotaModificada_H.SetForegroundColour(wx.Colour(60,60,160))
        self.label_quotaModificada_I.SetForegroundColour(wx.Colour(60,60,160))
        self.label_quotaModificada_J.SetForegroundColour(wx.Colour(60,60,160))
        self.label_quotaModificada_K.SetForegroundColour(wx.Colour(60,60,160))
        self.label_quotaModificada_L.SetForegroundColour(wx.Colour(60,60,160))
        self.label_quotaModificada_M.SetForegroundColour(wx.Colour(60,60,160))

        self.label_quotaModificadaArredondada_A.SetForegroundColour(wx.Colour(0,0,130))
        self.label_quotaModificadaArredondada_B.SetForegroundColour(wx.Colour(0,0,130))
        self.label_quotaModificadaArredondada_C.SetForegroundColour(wx.Colour(0,0,130))
        self.label_quotaModificadaArredondada_D.SetForegroundColour(wx.Colour(0,0,130))
        self.label_quotaModificadaArredondada_E.SetForegroundColour(wx.Colour(0,0,130))
        self.label_quotaModificadaArredondada_F.SetForegroundColour(wx.Colour(0,0,130))
        self.label_quotaModificadaArredondada_G.SetForegroundColour(wx.Colour(0,0,130))
        self.label_quotaModificadaArredondada_H.SetForegroundColour(wx.Colour(0,0,130))
        self.label_quotaModificadaArredondada_I.SetForegroundColour(wx.Colour(0,0,130))
        self.label_quotaModificadaArredondada_J.SetForegroundColour(wx.Colour(0,0,130))
        self.label_quotaModificadaArredondada_K.SetForegroundColour(wx.Colour(0,0,130))
        self.label_quotaModificadaArredondada_L.SetForegroundColour(wx.Colour(0,0,130))
        self.label_quotaModificadaArredondada_M.SetForegroundColour(wx.Colour(0,0,130))


    def numberEnterHandler(self, event):
        print('atum')


""" class temp():

    def clear():
        os.system('cls')

    def lista(ListaNumeros):
        clear()

        print("Introduz o numero. E depois a frequencia absoluta.")
        print("Quando terminares escreve *s*")
        print("Para apagar um numero escreve *n*")
        print("")
        print("Lista:")

        temp = ''

        for x in ListaNumeros:
            temp = temp + str(x) + '  '
        print(temp)
        print("")
        ListaTemporario = input()
        if ListaTemporario == "s":
            return ListaNumeros
        if ListaTemporario == "n":
            try:
                ListaNumeros.pop()
                lista(ListaNumeros)
            except:
                lista(ListaNumeros)
        try:
            try:
                ListaTemporario = int(ListaTemporario)
                ListaNumeros.append(int(ListaTemporario))
                lista(ListaNumeros)
            except:
                ListaTemporario = float(ListaTemporario)
                ListaNumeros.append(float(ListaTemporario))
                lista(ListaNumeros)
        except:
            if ListaTemporario != "s" and ListaTemporario != "n":
                print("Nao percebi esse ultimo.")
                time.sleep(0.8)
                lista(ListaNumeros)

    def cota(listaValores, valorDistribuir, bias):
        divisorPadrao = 0
        listaCotas = {}

        for x in listaValores:
            divisorPadrao += x
        
        divisorPadrao = divisorPadrao / valorDistribuir
        divisorPadrao += bias
        divisorPadrao = round(divisorPadrao, 3)

        for x in listaValores:
            cotaPadrao = x / divisorPadrao
            listaCotas[str(x)] = round(cotaPadrao, 0)   
        
        return divisorPadrao, listaCotas

    def total(listaCotas):
        valorTotal = 0
        for x in listaCotas:
            valorTotal += listaCotas[x]
        return valorTotal

    def resolucao(listaValores, done, valorDistribuir, bias):
        bias = round(bias, 3)
        # Calculacao das cotas
        divisorPadrao, listaCotas = cota(listaValores, valorDistribuir, bias)

        #check if it is correct
        valorTotal = total(listaCotas)
        if valorTotal == valorDistribuir:
            done = True
        elif valorTotal < valorDistribuir:
            bias -= 0.001
        elif valorTotal > valorDistribuir:
            bias += 0.001
        
        print(divisorPadrao)
        print(listaCotas)

    def calcular():
            # Declaracao de variveis
        listaValores = []

        # Aquisicao de valores
        lista(listaValores)
        clear()

        # Resolucao
        done = False
        valorDistribuir = 54
        bias = 0

        while not done:
            resolucao(listaValores, done, valorDistribuir, bias) """

if __name__ == "__main__":
    app = wx.App(False)
    frame = ProgramFrame()
    app.MainLoop()