class basicItems(object):
    """Establishes the framework for items found in player inventory"""
    def __init__(self,name,description,uses):
        self.Itemname=name
        self.ItemDesc=description
        self.itemUses=uses
    murder_items = ["Pillow","Knife","Gun"]
    Pillow = basicItems("pillow","Night night it is... number of uses",2)
    Knife = basicItems("knife","Didn't anyone ever tell you to be careful running around with knives? Number of uses", 2)
    Gun = basicItems ("gun","Ah, a classic one and done kind of deal. Number of uses",3)
 
# put 3 in to a list 
#creating the murderer items, could be placed in main file but going here for now for testing 
#Addendum: decided to create it in the class file instead
#"Pillow","Gun","Knife"
#Knife=basicItems("Knife","BLABLABLA THIS IS A TEST DESCRIPTION",2)
#Gun=basicItems("Gun","BLABLABLA THIS IS A TEST DESCRIPTION",3)
#Pillow=basicItems("Pillow","BLABLABLA THIS IS A TEST DESCRIPTION",1)



