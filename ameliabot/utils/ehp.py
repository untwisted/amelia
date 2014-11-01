from HTMLParser import HTMLParser
from collections import deque

version = '1.1'

DATA = 1
META = 2
COMMENT = 3
PI = 4
CODE = 5
AMP = 6

class Attribute(dict):
    """ This class inherits from dict. Here, the tag's attributes are held.
        They are printed at the right way.
        If you try to retrieve a key which does not exist it returns just '' which is
        an interesting behavior within this context.
    """

    def __getitem__(self, key):
        """ If self doesn't have the key it returns '' """

        if self.has_key(key):
            return dict.__getitem__(self, key)
        else:
            return ''

    def __str__(self):
        """ Returns a htmlized representation for attributes which are inside self."""
        data = str()

        for key, value in self.items():
            data += '%s="%s" ' % (key, value)

        return data

class Node(list):
    def __init__(self, name=None, attr={}):
        self.name = name
        self.attr = Attribute(attr)

        list.__init__(self)

    __repr__ = object.__repr__

    def __str__(self):
        """ This str function returns a string representation for the inner
            document.
        """

        html = ''

        for ind in self:
            html = html + str(ind)

        return html

    def sail(self):
        """ This method flattens the tree into a linear projection.
            It returns an interator which you can iterate over the tags which
            correspond to the documment. You can use it to filter tags and data.
        """
           
        for indi in self[:]:
            """
            copy = Node()
            copy.extend(indi)
            """

            for indj in indi.sail():
                yield(indj)

            yield(indi)

    def write(self, fname):
        fp = open(fname, 'w')
        content = str(self)

        fp.write(content)

        fp.close()

class Root(Node):
    """ This class holds all the tags inside the file regardless whether it has or not
        a <html> </html> tag.
        
        So, if you have a file like '''<html> contents </html> HELLO <em> WORLD </em>'''
        This class will hold the nodes html, data, em.

        As this class inherits from list you can add tags to the children as well as removing
        them just using del instance[index].
        You will be modifying the tree which was generated.
    """

    def sail_with_root(self):
        """ This one works alike the previous, however it yields the tag's parents as
            well as the child tag. This is useful when using insert_after and
            insert_before.
        """

        for indi in self[:]:
            """
            copy = Root()
            copy.extend(indi)
        
            if flag:
                yield((flag, indi))
            else:
                yield((self, indi))
            """

            for indj in indi.sail_with_root():
                yield(indj)

            yield((self, indi))

    def insert_after(self, y, k):
        """ Insert after a given tag. """
        ind = self.index(y)
        self.insert(ind + 1, k)

    def insert_before(self, y, k):
        """ Insert before a given tag. """
        ind = self.index(y)
        self.insert(ind, k)

    def easy(self):
        pointer = Easy(self)
        return pointer

class Tag(Root):
    """ This class corresponds to the representation of html's tag.
        It inherits from Root that is alike a Root class which holds all common
        properties between Tag, XTag(whose style is <tag />), and data text which is
        actually a class as well.
        As this tag inherits from Root. It permits you removing and
        adding tags as though you were working with lists.
    """

    def __init__(self, name, attr={}):
        Root.__init__(self)
        self.name = name
        self.attr = Attribute(attr)

    def __str__(self):
        """ This function returns a string representation for the class.
            It prints all the document for a given node/tag.
        """

        html = '\n<%s %s>\n' % (self.name, self.attr)
   

        for ind in self:
            html = html + str(ind)

        html = html + '\n</%s>' % self.name

        return html


class Data(Root):
    """ This class holds data that lies between tags. It is pretty much like a html's tag in 
        some aspects. So, if you are wnating to filter all text lying between tags
        from a given html document you just make a filter to filter all
        tags whose attribute is DATA.
    """

    def __init__(self, data):
        Root.__init__(self)
        self.name = DATA
        self.data = data

    def __str__(self):
        """ This function returns a string which correspond to the data inside the
            Data class.
        """

        return '\n' + self.data


class XTag(Root):
    """ This tag is the representation of html's tags in XHTML style like <img src="t.gif" />
        It is tags which do not have children.
    """

    def __str__(self):
        html = '\n<%s %s/>' % (self.name, self.attr)

        return html

class Meta(Root):
    """ Doctype """
    def __init__(self, data):
        Root.__init__(self)
        self.name = META
        self.data = data

    def __str__(self):
        html = '\n<!%s>' % self.data

        return html

class Code(Root):
    """ Doctype """
    def __init__(self, data):
        Root.__init__(self)
        self.name = CODE
        self.data = data

    def __str__(self):
        html = '\n&#%s' % self.data

        return html

class Amp(Root):
    """ Doctype """
    def __init__(self, data):
        Root.__init__(self)
        self.name = AMP
        self.data = data

    def __str__(self):
        html = '\n&%s' % self.data

        return html


class Pi(Root):
    def __init__(self, data):
        Root.__init__(self)
        self.name = PI
        self.data = data

    def __str__(self):
        html = '\n<?%s>' % self.data

        return html


class Comment(Root):
    def __init__(self, data):
        Root.__init__(self)
        self.name = COMMENT
        self.data = data

    def __str__(self):
        html = '\n<!--%s-->' % self.data

        return html



class Easy(Node):
    """ This class provides an easier interface to work with filters.
        It can make a great work when the filter's predicate is a bit complex.
        It is alike sail method but working with filter concept.
    """

    def __init__(self, master=Node()):
        Node.__init__(self)
        self.extend(master)

    def get_attr(self, key):
        """ This function returns a list with all the children's attributes corresponding
            to the given key

            Example:

            doc = Html()

            tree = doc.feed('''
                     <em style="background-color:red;">
                            Hello
                     </em>
  
                     <em style="background-color:blue;">
                            World.
                     </em>
                     <strong>
                            The life's sense.
                     </strong>
                    ''')

            base = tree.easy()

            print base['em'].get_attr()

            OUTPUT:

            ['background-color:red;', 'background-color:blue;']

        """

        pointer = list()

        for ind in self:
            pointer.append(ind.attr[key])

        return pointer

    def set_attr(self, key, value):
        """ This function is the get_attr's friend. It sets the attributes
            for all tags belonging to a given range which correspond to a given
            key.

            Example:
            doc = Html()

            tree = doc.feed('''
                     <em style="background-color:red;">
                            Hello
                     </em>
  
                     <em style="background-color:blue;">
                            World.
                     </em>
                     <strong>
                            The life's sense.
                     </strong>
                    ''')

            base = tree.easy()

            base['em'].set_attr('style', 'background-color:black;')
            base['em'].set_attr('newattr', 'newvalue')

            print tree

            OUTPUT:

            <em newattr="newvalue" style="background-color:black;" >
            Hello
            </em>
            <em newattr="newvalue" style="background-color:black;" >
            World
            </em>
            <strong >
            The life's sense.
            </strong>
        """


        for ind in self:
            ind.attr[key] = value


    def __getitem__(self, y):
        """ This function gets a list with all the children for a given
            filter's key. If y is a string then it works as a filter otherwise
            it returns the item at that index 
           
            Example: 

            doc = Html()
            tree = doc.feed('''<html>
                                    <head>

                                    </head>

                                    <body>
                                        <em> Example 1 </em>
                                        <strong> Example 2 </strong>
                                    </body>
                                </html>
                            ''')

            base = tree.easy()

            print base['html']['body']['em']
            
            OUTPUT:
            <em >
            Example 1
            </em>
            <em >
            Example 2
            </em>

            tag_em = base['html']['body']['em'][2]

            print tag_em

            <em >
                Example 2
            </em>

            Notice tag_em isn't of Easy's type it is Tag type
            So, you can't call set_attr and get_attr on tag_em.
            It happens when you strictly specify the tag inside the Easy's items.
        """

        if not isinstance(y, str):
            return Node.__getitem__(self, y)

        pointer = Easy()
        
        for indi in self:
            if indi.name == y:
                pointer.append(indi)

            for indj in indi.sail():
                if indj.name == y:
                    pointer.append(indj)

        return pointer

class Tree(object):
    """ This class is employed to build the documment's tree up.
        It nests the tags in a ordered way as they appear in the documment.
        It uses a stack to keep track of the tag's scope which is opened at the moment.
        When Html finds a closing tag it pops from the stack the actual pointer
        which corresponds to the actual scope then makes it point to the upmost
        tag's scope.
        Notice, when it finds a closing tag then it goes poping from the 
        stack till it achieves a the opening tag which corresponds to the closing tag.
        So, it understands tags from html documents whose closing tags are lacking
        like belonging to the outmost tag which is well formed it is having a opening tag
        and a closing tag as well.

        Lets feed it with the following html code.
        '''<body> <tag1> <tag2> <tag3> </tag1> <tag4> data </tag4></body> '''

        It would generate a tree whose structure would appear as.

        body -> tag1 -> ((tag2 -> tag3), tag4)
        
        So, tag1 would be inside tag1 that would hold just tag1 not tag3.
        and tag3 would be inside tag2 and tag4 would be inside tag1 too.
        It must try to reconstruct a html document from most broken html codes.
        and it will work according to this rule of precedence for tags.

        Tags which have just closing tags are just left aside. It doesn't create
        opening tags for them.
    """

    def __init__(self):
        """Initializes outmost which is the struct which will 
           hold all data inside the file.
        """

        self.outmost = Root()

        self.stack = deque()
        self.stack.append(self.outmost)

    def clear(self):
        """ Clear the outmost and stack for a new parsing """

        self.outmost = Root()
        self.stack.clear()
        self.stack.append(self.outmost)

    def last(self):
        """ Return the last pointer which point to the actual tag scope """
        return self.stack[-1]

    def nest(self, name, attr):
        """Nest a given tag at the bottom of the tree using 
           the last stack's pointer"""

        item = Tag(name, attr)

        pointer = self.stack.pop()

        pointer.append(item)

        self.stack.append(pointer)

        self.stack.append(item)

    def dnest(self, data):
        """ Nest the actual data onto the tree """

        top = self.last()

        item = Data(data)

        top.append(item)

    def xnest(self, name, attr):
        """ Nest a XTag onto the tree """

        top = self.last()

        item = XTag(name, attr)

        top.append(item)


    def ynest(self, data):
        top = self.last()

        item = Meta(data)

        top.append(item)


    def mnest(self, data):
        top = self.last()

        item = Comment(data)

        top.append(item)

    def cnest(self, data):
        top = self.last()

        item = Code(data)

        top.append(item)


    def rnest(self, data):
        top = self.last()

        item = Amp(data)

        top.append(item)


    def inest(self, data):
        top = self.last()

        item = Pi(data)

        top.append(item)

    def enclose(self, name):
        """ When found a closing tag then pops the pointer's scope from the stack
            so pointing to the earlier scope's tag.
        """

        count = 0

        for ind in reversed(self.stack):
            count = count + 1

            if ind.name == name:
                break
        else:
            count = 0

        """ Pops all the items which do not match with the closing tag. """
        for i in xrange(0, count):
            self.stack.pop()


class Html(HTMLParser):
    """ The main class"""

    def __init__(self):
        HTMLParser.__init__(self)
        self.struct = Tree()

    def fromfile(self, fname):
        fp = open(fname, 'r')

        content = fp.read()

        fp.close()

        return self.feed(content)

    def feed(self, data):
        self.struct.clear()
        HTMLParser.feed(self, data)

        return self.struct.outmost

    def handle_starttag(self, name, attr):
        """ When found a opening tag then nest it onto the tree """
        self.struct.nest(name, attr)
        pass

    def handle_startendtag(self, name, attr):
        """ When found a XHTML tag style then nest it up to the tree"""

        self.struct.xnest(name, attr)

    def handle_endtag(self, name):
        """ When found a closing tag then makes it point to the right scope """
        self.struct.enclose(name)
        pass

    def handle_data(self, data):
        """ Nest data onto the tree. """
        #tmp = data.rstrip()
        #tmp = tmp.strip()

        self.struct.dnest(data)    

    def handle_decl(self, decl):
        self.struct.ynest(decl)

    def unknown_decl(self, decl):
        self.struct.ynest(decl)

    def handle_charref(self, data):
        self.struct.cnest(data)

    def handle_entityref(self, data):
        self.struct.rnest(data)

    def handle_pi(self, data):
        self.struct.inest(data)

    def handle_comment(self, data):
        self.struct.mnest(data)

