
default money = 100
define l = Character("leopard", color="#dd9b15")
define e = Character("elephant", color='#aeb6b7')
define p = Character("pig", color='#ff5b5b')

image t = Tile("wind.jpg")

screen stats:
    vbox:
        text "Money: [money]" align (0.0, 0,0) color '#000000'

    
    
label start:

    scene t
    
    show screen stats
    show leo at truecenter

    l "I am a leopard"
    l "I want to transform into something"

    menu:
        "What should Leo transform into?"

        "Turn into an elephant (Costs $50)":

            jump elephant

        "Turn into a pig (Costs $20)":
            
            jump pig

label elephant:
    $ money -= 50
    hide leo
    show ele at truecenter
    e "I am now an elephant"
    return

label pig:
    $ money -= 20
    hide leo
    show pig at truecenter
    p "Oink I am a pig"
    return
 

    
