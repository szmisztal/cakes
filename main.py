import pickle
import glob
import types

class Cake:
    know_types = ['cake', 'muffin', 'meringue', 'biscuit', 'eclair', 'christmas', 'pretzel', 'other']
    bakery_offer = []

    def __init__(self, name, kind, taste, additives, filling, gluten_free, text):
        self.name = name
        if kind in Cake.know_types:
            self.kind = kind
        else:
            self.kind = 'other'
        self.taste = taste
        self.additives = additives
        self.filling = filling
        self.__gluten_free = gluten_free
        if kind == 'cake' or text == '':
            self.__text = text
        else:
            self.__text = ''
        Cake.bakery_offer.append(self)

    def show_info(self):
        print(f"Name: {self.name}".upper())
        print(f"Kind: {self.kind}")
        print(f"Taste: {self.taste}")
        if self.additives:
            print("Additives: ")
            for a in self.additives:
                print(f"\t{a}")
        if self.filling:
            print(f"Filling: {self.filling}")
        print(f"Gluten free: {self.__gluten_free}")
        print(f"Text available: {self.__text}")
        print('-' * 30)

    def set_filling(self, filling):
        self.filling = filling

    def add_additives(self, additives):
        self.additives.extend(additives)

    @property
    def text_set(self):
        return self.__text

    @text_set.setter
    def text_set(self, new_text):
        if self.kind == 'cake':
            self.__text = new_text
        else:
            print(f"Cannot add text: '{new_text}' for {self.name}.")

    def save_to_file(self, path):
        with open(path, 'wb') as f:
            pickle.dump(self, f)

    @classmethod
    def read_from_file(cls, path):
        with open(path, 'rb') as f:
            new_cake = pickle.load(f)
        cls.bakery_offer.append(new_cake)
        return new_cake

    @staticmethod
    def get_bakery_files(catalog):
        return glob.glob(catalog+'/*.bakery')


cake_1 = Cake('Vanilla Cake', 'cake', 'vanilla', [], '', True, 'Happy Birthday !')
cake_2 = Cake('Chocolate Muffin', 'muffin', 'chocolate', [], '', False, '')
cake_3 = Cake('Super Sweet Meringue', 'meringue', 'very sweet', ['nuts', 'cream', 'lemon'], '', False, '')
cake_4 = Cake('Cocoa waffle', 'waffle', 'cocoa', [], 'cocoa', True, 'Happy Wedding !')

cake_1.add_additives(['cocoa powder', 'sugar'])
cake_1.set_filling('vanilla')
cake_2.add_additives(['cream'])
cake_2.set_filling('white chocolate')
cake_3.set_filling('nuts')
cake_1.text_set = "Happy Wedding !"
cake_4.text_set = "Happy Birthday !"

def export_1_cake_to_html(obj, path):
    template = """
<table border=1>
     <tr>
       <th colspan=2>{}</th>
     </tr>
       <tr>
         <td>Kind</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Taste</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Additives</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Filling</td>
         <td>{}</td>
       </tr>
</table>"""

    with open(path, "w") as f:
        content = template.format(obj.name, obj.kind, obj.taste, obj.additives, obj.filling)
        f.write(content)


def export_all_cakes_to_html(cls, path):
    template_header = """
<table border=1>"""
    template_data="""
     <tr>
       <th colspan=2>{}</th>
     </tr>
     <tr>
         <td>Kind</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Taste</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Additives</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Filling</td>
         <td>{}</td>
       </tr>"""
    template_footer="""</indent>
</table>"""
    with open(path, "w") as f:
        f.write(template_header)
        for c in cls.bakery_offer:
            content = template_data.format(c.name, c.kind, c.taste, c.additives, c.filling)
            f.write(content)
        f.write(template_footer)



def export_this_cake_to_html(self, path):
    template = """
<table border=1>
     <tr>
       <th colspan=2>{}</th>
     </tr>
       <tr>
         <td>Kind</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Taste</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Additives</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Filling</td>
         <td>{}</td>
       </tr>
</table>"""

    with open(path, "w") as f:
        content = template.format(self.name, self.kind, self.taste, self.additives, self.filling)
        f.write(content)

#static method:
Cake.export_1_cake_to_html = export_1_cake_to_html
Cake.export_1_cake_to_html(cake_1, 'c:/programy/python/zadania/cakes/cake_1.html')

#class method:
Cake.export_all_cakes_to_html = types.MethodType(export_all_cakes_to_html, Cake)
Cake.export_all_cakes_to_html('c:/programy/python/zadania/cakes/all_cakes.html')

#instance method:
for c in Cake.bakery_offer:
    c.export_this_cake_to_html = types.MethodType(export_this_cake_to_html, c)
for c in Cake.bakery_offer:
    c.export_this_cake_to_html('c:/programy/python/zadania/cakes/{}.html'.format(c.name.replace(' ','_')))

