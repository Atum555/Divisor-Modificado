import wx

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
        font_B = wx.Font(20, wx.FONTFAMILY_SWISS, wx.NORMAL, wx.FONTWEIGHT_SEMIBOLD, False, u'Consolas')
        font_C = wx.Font(15, wx.MODERN, wx.NORMAL, wx.FONTWEIGHT_LIGHT, False, u'Consolas')

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


        # Add Total Values
        label_totalValores_label = wx.StaticText(
            self, label='Total: ',
            pos=(10,530), size=(50,35), style= wx.ALIGN_LEFT
        )
        label_totalValores_label.SetFont(font_B)


        self.label_totalValores_value = wx.StaticText(
            self, label='14542',
            pos=(160,535), size=(80,35), style= wx.ALIGN_RIGHT
        )
        self.label_totalValores_value.SetFont(font_A)


        self.label_totalPadrao = wx.StaticText(
            self, label='2186',
            pos=(445,535), size=(50,35), style= wx.ALIGN_CENTER
        )
        self.label_totalPadrao.SetFont(font_A)


        self.label_totalModificado = wx.StaticText(
            self, label='6332',
            pos=(833,535), size=(80,35), style= wx.ALIGN_CENTER
        )
        self.label_totalModificado.SetFont(font_A)


        # Add Valor a Dividir
        label_valorDividir = wx.StaticText(
            self, label='Repartir: ',
            pos=(10,575), size=(50,35), style= wx.ALIGN_LEFT
        )
        label_valorDividir.SetFont(font_C)


        self.textBox_valorDividir = wx.TextCtrl(
            self, value='',
            pos=(120,575), size=(120,25), 
            style=wx.TE_RICH | wx.TE_PROCESS_ENTER
        )
        self.textBox_valorDividir.SetFont(font_A)
        self.Bind(
            event=wx.EVT_TEXT,
            handler=self.numberEnterHandler,
            source=self.textBox_valorDividir
        )


        # Add Divisores
        label_divisor_label = wx.StaticText(
            self, label='Divisor: ',
            pos=(300,575), size=(50,35), style= wx.ALIGN_LEFT
        )
        label_divisor_label.SetFont(font_C)


        self.label_divisorPadrao_value = wx.StaticText(
            self, label='164',
            pos=(430,575), size=(80,35), style= wx.ALIGN_CENTER
        )
        self.label_divisorPadrao_value.SetFont(font_C)


        self.label_divisorModificado_value = wx.StaticText(
            self, label='147',
            pos=(832,575), size=(80,35), style= wx.ALIGN_CENTER
        )
        self.label_divisorModificado_value.SetFont(font_C)


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


        # Color
        self.label_totalValores_value.SetForegroundColour(wx.Colour(90,90,90))
        self.label_totalPadrao.SetForegroundColour(wx.Colour(90,90,90))
        self.label_totalModificado.SetForegroundColour(wx.Colour(90,90,90))

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

    def clearAllValues(self):
        self.label_quotaPadrao_A.SetLabel('')
        self.label_quotaPadrao_B.SetLabel('')
        self.label_quotaPadrao_C.SetLabel('')
        self.label_quotaPadrao_D.SetLabel('')
        self.label_quotaPadrao_E.SetLabel('')
        self.label_quotaPadrao_F.SetLabel('')
        self.label_quotaPadrao_G.SetLabel('')
        self.label_quotaPadrao_H.SetLabel('')
        self.label_quotaPadrao_I.SetLabel('')
        self.label_quotaPadrao_J.SetLabel('')
        self.label_quotaPadrao_K.SetLabel('')
        self.label_quotaPadrao_L.SetLabel('')
        
        self.label_quotaPadraoArredondada_A.SetLabel('')
        self.label_quotaPadraoArredondada_B.SetLabel('')
        self.label_quotaPadraoArredondada_C.SetLabel('')
        self.label_quotaPadraoArredondada_D.SetLabel('')
        self.label_quotaPadraoArredondada_E.SetLabel('')
        self.label_quotaPadraoArredondada_F.SetLabel('')
        self.label_quotaPadraoArredondada_G.SetLabel('')
        self.label_quotaPadraoArredondada_H.SetLabel('')
        self.label_quotaPadraoArredondada_I.SetLabel('')
        self.label_quotaPadraoArredondada_J.SetLabel('')
        self.label_quotaPadraoArredondada_K.SetLabel('')
        self.label_quotaPadraoArredondada_L.SetLabel('')

        self.label_quotaModificada_A.SetLabel('')
        self.label_quotaModificada_B.SetLabel('')
        self.label_quotaModificada_C.SetLabel('')
        self.label_quotaModificada_D.SetLabel('')
        self.label_quotaModificada_E.SetLabel('')
        self.label_quotaModificada_F.SetLabel('')
        self.label_quotaModificada_G.SetLabel('')
        self.label_quotaModificada_H.SetLabel('')
        self.label_quotaModificada_I.SetLabel('')
        self.label_quotaModificada_J.SetLabel('')
        self.label_quotaModificada_K.SetLabel('')
        self.label_quotaModificada_L.SetLabel('')

        self.label_quotaModificadaArredondada_A.SetLabel('')
        self.label_quotaModificadaArredondada_B.SetLabel('')
        self.label_quotaModificadaArredondada_C.SetLabel('')
        self.label_quotaModificadaArredondada_D.SetLabel('')
        self.label_quotaModificadaArredondada_E.SetLabel('')
        self.label_quotaModificadaArredondada_F.SetLabel('')
        self.label_quotaModificadaArredondada_G.SetLabel('')
        self.label_quotaModificadaArredondada_H.SetLabel('')
        self.label_quotaModificadaArredondada_I.SetLabel('')
        self.label_quotaModificadaArredondada_J.SetLabel('')
        self.label_quotaModificadaArredondada_K.SetLabel('')
        self.label_quotaModificadaArredondada_L.SetLabel('')

        self.label_totalValores_value.SetLabel('')
        self.label_totalPadrao.SetLabel('')
        self.label_totalModificado.SetLabel('')

        self.label_divisorPadrao_value.SetLabel('')
        self.label_divisorModificado_value.SetLabel('')

    def checkDividir(self):
        if self.textBox_valorDividir.GetValue():
            try:
                int(self.textBox_valorDividir.GetValue())
                self.textBox_valorDividir.SetBackgroundColour(wx.Colour(255,255,255))
                self.valorDividir = int(self.textBox_valorDividir.GetValue())
                return True
            except:
                pass
        self.textBox_valorDividir.SetBackgroundColour(wx.Colour(255,0,0))
        return False

    def getValues(self):
        if self.textBox_A.GetValue():
            try: 
                int(self.textBox_A.GetValue())
                self.textBox_A.SetBackgroundColour(wx.Colour(255,255,255))
                self.values['A'] = [True, int(self.textBox_A.GetValue()), 0, 0, 0, 0]
            except:
                self.values['A'] = [False, 0, 0, 0, 0, 0]
                self.textBox_A.SetBackgroundColour(wx.Colour(255,0,0))
        else:
            self.textBox_A.SetBackgroundColour(wx.Colour(255,255,255))
            self.values['A'] = [False, 0, 0, 0, 0, 0]


        if self.textBox_B.GetValue():
            try:
                int(self.textBox_B.GetValue())
                self.textBox_B.SetBackgroundColour(wx.Colour(255,255,255))
                self.values['B'] = [True, int(self.textBox_B.GetValue()), 0, 0, 0, 0]
            except:
                self.values['B'] = [False, 0, 0, 0, 0, 0]
                self.textBox_B.SetBackgroundColour(wx.Colour(255,0,0))
        else:
            self.textBox_B.SetBackgroundColour(wx.Colour(255,255,255))
            self.values['B'] = [False, 0, 0, 0, 0, 0]

        
        if self.textBox_C.GetValue():
            try:
                int(self.textBox_C.GetValue())
                self.textBox_C.SetBackgroundColour(wx.Colour(255,255,255))
                self.values['C'] = [True, int(self.textBox_C.GetValue()), 0, 0, 0, 0]
            except:
                self.values['C'] = [False, 0, 0, 0, 0, 0]
                self.textBox_C.SetBackgroundColour(wx.Colour(255,0,0))
        else:
            self.textBox_C.SetBackgroundColour(wx.Colour(255,255,255))
            self.values['C'] = [False, 0, 0, 0, 0, 0]
        

        if self.textBox_D.GetValue():
            try:
                int(self.textBox_D.GetValue())
                self.textBox_D.SetBackgroundColour(wx.Colour(255,255,255))
                self.values['D'] = [True, int(self.textBox_D.GetValue()), 0, 0, 0, 0]
            except:
                self.values['D'] = [False, 0, 0, 0, 0, 0]
                self.textBox_D.SetBackgroundColour(wx.Colour(255,0,0))
        else:
            self.textBox_D.SetBackgroundColour(wx.Colour(255,255,255))
            self.values['D'] = [False, 0, 0, 0, 0, 0]


        if self.textBox_E.GetValue():
            try:
                int(self.textBox_E.GetValue())
                self.textBox_E.SetBackgroundColour(wx.Colour(255,255,255))
                self.values['E'] = [True, int(self.textBox_E.GetValue()), 0, 0, 0, 0]
            except:
                self.values['E'] = [False, 0, 0, 0, 0, 0]
                self.textBox_E.SetBackgroundColour(wx.Colour(255,0,0))
        else:
            self.textBox_E.SetBackgroundColour(wx.Colour(255,255,255))
            self.values['E'] = [False, 0, 0, 0, 0, 0]
        

        if self.textBox_F.GetValue():
            try:
                int(self.textBox_F.GetValue())
                self.textBox_F.SetBackgroundColour(wx.Colour(255,255,255))
                self.values['F'] = [True, int(self.textBox_F.GetValue()), 0, 0, 0, 0]
            except:
                self.values['F'] = [False, 0, 0, 0, 0, 0]
                self.textBox_F.SetBackgroundColour(wx.Colour(255,0,0))
        else:
            self.textBox_F.SetBackgroundColour(wx.Colour(255,255,255))
            self.values['F'] = [False, 0, 0, 0, 0, 0]


        if self.textBox_G.GetValue():
            try:
                int(self.textBox_G.GetValue())
                self.textBox_G.SetBackgroundColour(wx.Colour(255,255,255))
                self.values['G'] = [True, int(self.textBox_G.GetValue()), 0, 0, 0, 0]
            except:
                self.values['G'] = [False, 0, 0, 0, 0, 0]
                self.textBox_G.SetBackgroundColour(wx.Colour(255,0,0))
        else:
            self.textBox_G.SetBackgroundColour(wx.Colour(255,255,255))
            self.values['G'] = [False, 0, 0, 0, 0, 0]

        
        if self.textBox_H.GetValue():
            try:
                int(self.textBox_H.GetValue())
                self.textBox_H.SetBackgroundColour(wx.Colour(255,255,255))
                self.values['H'] = [True, int(self.textBox_H.GetValue()), 0, 0, 0, 0]
            except:
                self.values['H'] = [False, 0, 0, 0, 0, 0]
                self.textBox_H.SetBackgroundColour(wx.Colour(255,0,0))
        else:
            self.textBox_H.SetBackgroundColour(wx.Colour(255,255,255))
            self.values['H'] = [False, 0, 0, 0, 0, 0]


        if self.textBox_I.GetValue():
            try:
                int(self.textBox_I.GetValue())
                self.textBox_I.SetBackgroundColour(wx.Colour(255,255,255))
                self.values['I'] = [True, int(self.textBox_I.GetValue()), 0, 0, 0, 0]
            except:
                self.values['I'] = [False, 0, 0, 0, 0, 0]
                self.textBox_I.SetBackgroundColour(wx.Colour(255,0,0))
        else:
            self.textBox_I.SetBackgroundColour(wx.Colour(255,255,255))
            self.values['I'] = [False, 0, 0, 0, 0, 0]


        if self.textBox_J.GetValue():
            try:
                int(self.textBox_J.GetValue())
                self.textBox_A.SetBackgroundColour(wx.Colour(255,255,255))
                self.values['J'] = [True, int(self.textBox_J.GetValue()), 0, 0, 0, 0]
            except:
                self.values['J'] = [False, 0, 0, 0, 0, 0]
                self.textBox_J.SetBackgroundColour(wx.Colour(255,0,0))
        else:
            self.textBox_J.SetBackgroundColour(wx.Colour(255,255,255))
            self.values['J'] = [False, 0, 0, 0, 0, 0]


        if self.textBox_K.GetValue():
            try:
                int(self.textBox_K.GetValue())
                self.textBox_K.SetBackgroundColour(wx.Colour(255,255,255))
                self.values['K'] = [True, int(self.textBox_K.GetValue()), 0, 0, 0, 0]
            except:
                self.values['K'] = [False, 0, 0, 0, 0, 0]
                self.textBox_K.SetBackgroundColour(wx.Colour(255,0,0))
        else:
            self.textBox_K.SetBackgroundColour(wx.Colour(255,255,255))
            self.values['K'] = [False, 0, 0, 0, 0, 0]


        if self.textBox_L.GetValue():
            try:
                int(self.textBox_L.GetValue())
                self.textBox_L.SetBackgroundColour(wx.Colour(255,255,255))
                self.values['L'] = [True, int(self.textBox_L.GetValue()), 0, 0, 0, 0]
            except:
                self.values['L'] = [False, 0, 0, 0, 0, 0]
                self.textBox_L.SetBackgroundColour(wx.Colour(255,0,0))
        else:
            self.textBox_L.SetBackgroundColour(wx.Colour(255,255,255))
            self.values['L'] = [False, 0, 0, 0, 0, 0]

    def totalValues(self):
        total = 0
        for x in self.values:
            if self.values[x][0]:
                total += self.values[x][1]
        if total != 0:
            self.label_totalValores_value.SetLabel(str(total))
        self.totalValues_value = total
        
    def calDivisorPadrao(self):
        self.divisorPadrao = self.totalValues_value / self.valorDividir
        if self.divisorPadrao != 0:
            self.label_divisorPadrao_value.SetLabel(str(round(self.divisorPadrao, 3)))
            return
        self.label_divisorPadrao_value.SetLabel('')

    def calCotaPadrao(self):
        if self.values['A'][0]:
            self.values['A'][2] = self.values['A'][1] / self.divisorPadrao
            self.label_quotaPadrao_A.SetLabel(str(round(self.values['A'][2], 3)))

        if self.values['B'][0]:
            self.values['B'][2] = self.values['B'][1] / self.divisorPadrao
            self.label_quotaPadrao_B.SetLabel(str(round(self.values['B'][2], 3)))

        if self.values['C'][0]:
            self.values['C'][2] = self.values['C'][1] / self.divisorPadrao
            self.label_quotaPadrao_C.SetLabel(str(round(self.values['C'][2], 3)))

        if self.values['D'][0]:
            self.values['D'][2] = self.values['D'][1] / self.divisorPadrao
            self.label_quotaPadrao_D.SetLabel(str(round(self.values['D'][2], 3)))

        if self.values['E'][0]:
            self.values['E'][2] = self.values['E'][1] / self.divisorPadrao
            self.label_quotaPadrao_E.SetLabel(str(round(self.values['E'][2], 3)))

        if self.values['F'][0]:
            self.values['F'][2] = self.values['F'][1] / self.divisorPadrao
            self.label_quotaPadrao_F.SetLabel(str(round(self.values['F'][2], 3)))

        if self.values['G'][0]:
            self.values['G'][2] = self.values['G'][1] / self.divisorPadrao
            self.label_quotaPadrao_G.SetLabel(str(round(self.values['G'][2], 3)))

        if self.values['H'][0]:
            self.values['H'][2] = self.values['H'][1] / self.divisorPadrao
            self.label_quotaPadrao_H.SetLabel(str(round(self.values['H'][2], 3)))
        
        if self.values['I'][0]:
            self.values['I'][2] = self.values['I'][1] / self.divisorPadrao
            self.label_quotaPadrao_I.SetLabel(str(round(self.values['I'][2], 3)))

        if self.values['J'][0]:
            self.values['J'][2] = self.values['J'][1] / self.divisorPadrao
            self.label_quotaPadrao_J.SetLabel(str(round(self.values['J'][2], 3)))

        if self.values['K'][0]:
            self.values['K'][2] = self.values['K'][1] / self.divisorPadrao
            self.label_quotaPadrao_K.SetLabel(str(round(self.values['K'][2], 3)))

        if self.values['L'][0]:
            self.values['L'][2] = self.values['L'][1] / self.divisorPadrao
            self.label_quotaPadrao_L.SetLabel(str(round(self.values['L'][2], 3)))

    def calCotaPadraoArr(self):
        for x in self.values:
            if self.values[x][0]:
                self.values[x][3] = int(round(self.values[x][2], 0))

        if self.values['A'][0]:
            self.label_quotaPadraoArredondada_A.SetLabel(str(self.values['A'][3]))

        if self.values['B'][0]:
            self.label_quotaPadraoArredondada_B.SetLabel(str(self.values['B'][3]))

        if self.values['C'][0]:
            self.label_quotaPadraoArredondada_C.SetLabel(str(self.values['C'][3]))

        if self.values['D'][0]:
            self.label_quotaPadraoArredondada_D.SetLabel(str(self.values['D'][3]))

        if self.values['E'][0]:
            self.label_quotaPadraoArredondada_E.SetLabel(str(self.values['E'][3]))

        if self.values['F'][0]:
            self.label_quotaPadraoArredondada_F.SetLabel(str(self.values['F'][3]))

        if self.values['G'][0]:
            self.label_quotaPadraoArredondada_G.SetLabel(str(self.values['G'][3]))

        if self.values['H'][0]:
            self.label_quotaPadraoArredondada_H.SetLabel(str(self.values['H'][3]))

        if self.values['I'][0]:
            self.label_quotaPadraoArredondada_I.SetLabel(str(self.values['I'][3]))

        if self.values['J'][0]:
            self.label_quotaPadraoArredondada_J.SetLabel(str(self.values['J'][3]))

        if self.values['K'][0]:
            self.label_quotaPadraoArredondada_K.SetLabel(str(self.values['K'][3]))

        if self.values['L'][0]:
            self.label_quotaPadraoArredondada_L.SetLabel(str(self.values['L'][3]))

    def totalPadrao(self):
        totalPadrao = 0 
        for x in self.values:
            if self.values[x][0]:
                totalPadrao += self.values[x][3]
        if totalPadrao != 0:
            self.label_totalPadrao.SetLabel(str(totalPadrao))
            self.totalPadrao_value = totalPadrao
            return
        self.totalPadrao_value = 0

    def checkCotaModificada(self):
        if self.totalModificada_value == self.valorDividir:
            return True
        else:
            return False

    def biasUpdater(self):
        if self.totalModificada_value > self.valorDividir:
            return True
        if self.totalModificada_value < self.valorDividir:
            return False

    def updateCotaModificada_Value(self):
        if self.values['A'][0]:
            self.values['A'][4] = self.values['A'][1] / self.tempDivisorPadrao
            self.values['A'][5] =  round(self.values['A'][4], 0)

        if self.values['B'][0]:
            self.values['B'][4] = self.values['B'][1] / self.tempDivisorPadrao
            self.values['B'][5] =  round(self.values['B'][4], 0)

        if self.values['C'][0]:
            self.values['C'][4] = self.values['C'][1] / self.tempDivisorPadrao
            self.values['C'][5] =  round(self.values['C'][4], 0)

        if self.values['D'][0]:
            self.values['D'][4] = self.values['D'][1] / self.tempDivisorPadrao
            self.values['D'][5] =  round(self.values['D'][4], 0)

        if self.values['E'][0]:
            self.values['E'][4] = self.values['E'][1] / self.tempDivisorPadrao
            self.values['E'][5] =  round(self.values['E'][4], 0)

        if self.values['F'][0]:
            self.values['F'][4] = self.values['F'][1] / self.tempDivisorPadrao
            self.values['F'][5] =  round(self.values['F'][4], 0)

        if self.values['G'][0]:
            self.values['G'][4] = self.values['G'][1] / self.tempDivisorPadrao
            self.values['G'][5] =  round(self.values['G'][4], 0)

        if self.values['H'][0]:
            self.values['H'][4] = self.values['H'][1] / self.tempDivisorPadrao
            self.values['H'][5] =  round(self.values['H'][4], 0)

        if self.values['I'][0]:
            self.values['I'][4] = self.values['I'][1] / self.tempDivisorPadrao
            self.values['I'][5] =  round(self.values['I'][4], 0)

        if self.values['J'][0]:
            self.values['J'][4] = self.values['J'][1] / self.tempDivisorPadrao
            self.values['J'][5] =  round(self.values['J'][4], 0)

        if self.values['K'][0]:
            self.values['K'][4] = self.values['K'][1] / self.tempDivisorPadrao
            self.values['K'][5] =  round(self.values['K'][4], 0)

        if self.values['L'][0]:
            self.values['L'][4] = self.values['L'][1] / self.tempDivisorPadrao
            self.values['L'][5] =  round(self.values['L'][4], 0)

        self.totalModificada_value = 0 
        for x in self.values:
            if self.values[x][0]:
                self.totalModificada_value += self.values[x][5]

    def calCotaModificada(self):
        for x in self.values:
            if self.values[x][0]:
                self.values[x][4] = self.values[x][2]
                self.values[x][5] = self.values[x][3]

        self.totalModificada_value = self.totalPadrao_value
        counter = 0
        self.tempDivisorPadrao = self.divisorPadrao
        self.tempDivisorPadrao = round(self.tempDivisorPadrao, 1)

        if not self.checkCotaModificada():
            bias = self.biasUpdater()
        
        while not self.checkCotaModificada() and not counter > 10000 :
            counter += 1
            biasTemp = bias
            bias = self.biasUpdater()
            if not bias == biasTemp:
                break
            if bias:
                self.tempDivisorPadrao += 0.1
            else:
                self.tempDivisorPadrao -= 0.1
            self.updateCotaModificada_Value()

        if not self.checkCotaModificada():
            self.tempDivisorPadrao = self.divisorPadrao
            self.tempDivisorPadrao = round(self.tempDivisorPadrao, 2)

        while not self.checkCotaModificada() and not counter > 10000 :
            counter += 1
            biasTemp = bias
            bias = self.biasUpdater()
            if not bias == biasTemp:
                break
            if bias:
                self.tempDivisorPadrao += 0.01
            else:
                self.tempDivisorPadrao -= 0.01
            self.updateCotaModificada_Value()

        if not self.checkCotaModificada():
            self.tempDivisorPadrao = self.divisorPadrao
            self.tempDivisorPadrao = round(self.tempDivisorPadrao, 3)
            
        while not self.checkCotaModificada() and not counter > 10000 :
            counter += 1
            biasTemp = bias
            bias = self.biasUpdater()
            if not bias == biasTemp:
                break
            if bias:
                self.tempDivisorPadrao += 0.001
            else:
                self.tempDivisorPadrao -= 0.001
            self.updateCotaModificada_Value()

    def showCotaModificada(self):
        if self.values['A'][0]:
            self.label_quotaModificada_A.SetLabel(str(round(self.values['A'][4], 3)))

        if self.values['B'][0]:
            self.label_quotaModificada_B.SetLabel(str(round(self.values['B'][4], 3)))

        if self.values['C'][0]:
            self.label_quotaModificada_C.SetLabel(str(round(self.values['C'][4], 3)))

        if self.values['D'][0]:
            self.label_quotaModificada_D.SetLabel(str(round(self.values['D'][4], 3)))

        if self.values['E'][0]:
            self.label_quotaModificada_E.SetLabel(str(round(self.values['E'][4], 3)))

        if self.values['F'][0]:
            self.label_quotaModificada_F.SetLabel(str(round(self.values['F'][4], 3)))

        if self.values['G'][0]:
            self.label_quotaModificada_G.SetLabel(str(round(self.values['G'][4], 3)))

        if self.values['H'][0]:
            self.label_quotaModificada_H.SetLabel(str(round(self.values['H'][4], 3)))

        if self.values['I'][0]:
            self.label_quotaModificada_I.SetLabel(str(round(self.values['I'][4], 3)))

        if self.values['J'][0]:
            self.label_quotaModificada_J.SetLabel(str(round(self.values['J'][4], 3)))

        if self.values['K'][0]:
            self.label_quotaModificada_K.SetLabel(str(round(self.values['K'][4], 3)))

        if self.values['L'][0]:
            self.label_quotaModificada_L.SetLabel(str(round(self.values['L'][4], 3)))

    def showCotaModificadaArr(self):
        if self.values['A'][0]:
            self.label_quotaModificadaArredondada_A.SetLabel(str(int(self.values['A'][5])))

        if self.values['B'][0]:
            self.label_quotaModificadaArredondada_B.SetLabel(str(int(self.values['B'][5])))

        if self.values['C'][0]:
            self.label_quotaModificadaArredondada_C.SetLabel(str(int(self.values['C'][5])))

        if self.values['D'][0]:
            self.label_quotaModificadaArredondada_D.SetLabel(str(int(self.values['D'][5])))

        if self.values['E'][0]:
            self.label_quotaModificadaArredondada_E.SetLabel(str(int(self.values['E'][5])))

        if self.values['F'][0]:
            self.label_quotaModificadaArredondada_F.SetLabel(str(int(self.values['F'][5])))

        if self.values['G'][0]:
            self.label_quotaModificadaArredondada_G.SetLabel(str(int(self.values['G'][5])))

        if self.values['H'][0]:
            self.label_quotaModificadaArredondada_H.SetLabel(str(int(self.values['H'][5])))

        if self.values['I'][0]:
            self.label_quotaModificadaArredondada_I.SetLabel(str(int(self.values['I'][5])))

        if self.values['J'][0]:
            self.label_quotaModificadaArredondada_J.SetLabel(str(int(self.values['J'][5])))

        if self.values['K'][0]:
            self.label_quotaModificadaArredondada_K.SetLabel(str(int(self.values['K'][5])))

        if self.values['L'][0]:
            self.label_quotaModificadaArredondada_L.SetLabel(str(int(self.values['L'][5])))
    
    def showTotalCotaModificada(self):
        if self.totalModificada_value != 0:
            self.label_totalModificado.SetLabel(str(int(self.totalModificada_value)))

    def showDivisorModificado(self):
        if self.tempDivisorPadrao != 0:
            self.label_divisorModificado_value.SetLabel(str(round(self.tempDivisorPadrao, 3)))

    def showModificados(self):
        if self.checkCotaModificada():
            self.showCotaModificada()
            self.showCotaModificadaArr()
            self.showTotalCotaModificada()
            self.showDivisorModificado()

    def numberEnterHandler(self, event):
        self.clearAllValues()
        if not self.checkDividir():
            return
        self.values = {}
        self.getValues()
        self.totalValues()
        self.calDivisorPadrao()
        self.calCotaPadrao()
        self.calCotaPadraoArr()
        self.totalPadrao()
        self.calCotaModificada()
        self.showModificados()
        print(self.values)

if __name__ == "__main__":
    app = wx.App(False)
    frame = ProgramFrame()
    app.MainLoop()