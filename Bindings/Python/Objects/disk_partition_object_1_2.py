#!/usr/bin/env python
# -*- coding: utf-8 -*- 

#
# Generated Tue Apr 10 13:54:50 2012 by generateDS.py version 2.7b.
#

import sys
import getopt
import re as re_
import common_types_1_0 as common

etree_ = None
Verbose_import_ = False
(   XMLParser_import_none, XMLParser_import_lxml,
    XMLParser_import_elementtree
    ) = range(3)
XMLParser_import_library = None
try:
    # lxml
    from lxml import etree as etree_
    XMLParser_import_library = XMLParser_import_lxml
    if Verbose_import_:
        print("running with lxml.etree")
except ImportError:
    try:
        # cElementTree from Python 2.5+
        import xml.etree.cElementTree as etree_
        XMLParser_import_library = XMLParser_import_elementtree
        if Verbose_import_:
            print("running with cElementTree on Python 2.5+")
    except ImportError:
        try:
            # ElementTree from Python 2.5+
            import xml.etree.ElementTree as etree_
            XMLParser_import_library = XMLParser_import_elementtree
            if Verbose_import_:
                print("running with ElementTree on Python 2.5+")
        except ImportError:
            try:
                # normal cElementTree install
                import cElementTree as etree_
                XMLParser_import_library = XMLParser_import_elementtree
                if Verbose_import_:
                    print("running with cElementTree")
            except ImportError:
                try:
                    # normal ElementTree install
                    import elementtree.ElementTree as etree_
                    XMLParser_import_library = XMLParser_import_elementtree
                    if Verbose_import_:
                        print("running with ElementTree")
                except ImportError:
                    raise ImportError("Failed to import ElementTree from any known place")

def parsexml_(*args, **kwargs):
    if (XMLParser_import_library == XMLParser_import_lxml and
        'parser' not in kwargs):
        # Use the lxml ElementTree compatible parser so that, e.g.,
        #   we ignore comments.
        kwargs['parser'] = etree_.ETCompatXMLParser()
    doc = etree_.parse(*args, **kwargs)
    return doc

#
# User methods
#
# Calls to the methods in these classes are generated by generateDS.py.
# You can replace these methods by re-implementing the following class
#   in a module named generatedssuper.py.

try:
    from generatedssuper import GeneratedsSuper
except ImportError, exp:

    class GeneratedsSuper(object):
        def gds_format_string(self, input_data, input_name=''):
            return input_data
        def gds_validate_string(self, input_data, node, input_name=''):
            return input_data
        def gds_format_integer(self, input_data, input_name=''):
            return '%d' % input_data
        def gds_validate_integer(self, input_data, node, input_name=''):
            return input_data
        def gds_format_integer_list(self, input_data, input_name=''):
            return '%s' % input_data
        def gds_validate_integer_list(self, input_data, node, input_name=''):
            values = input_data.split()
            for value in values:
                try:
                    fvalue = float(value)
                except (TypeError, ValueError), exp:
                    raise_parse_error(node, 'Requires sequence of integers')
            return input_data
        def gds_format_float(self, input_data, input_name=''):
            return '%f' % input_data
        def gds_validate_float(self, input_data, node, input_name=''):
            return input_data
        def gds_format_float_list(self, input_data, input_name=''):
            return '%s' % input_data
        def gds_validate_float_list(self, input_data, node, input_name=''):
            values = input_data.split()
            for value in values:
                try:
                    fvalue = float(value)
                except (TypeError, ValueError), exp:
                    raise_parse_error(node, 'Requires sequence of floats')
            return input_data
        def gds_format_double(self, input_data, input_name=''):
            return '%e' % input_data
        def gds_validate_double(self, input_data, node, input_name=''):
            return input_data
        def gds_format_double_list(self, input_data, input_name=''):
            return '%s' % input_data
        def gds_validate_double_list(self, input_data, node, input_name=''):
            values = input_data.split()
            for value in values:
                try:
                    fvalue = float(value)
                except (TypeError, ValueError), exp:
                    raise_parse_error(node, 'Requires sequence of doubles')
            return input_data
        def gds_format_boolean(self, input_data, input_name=''):
            return '%s' % input_data
        def gds_validate_boolean(self, input_data, node, input_name=''):
            return input_data
        def gds_format_boolean_list(self, input_data, input_name=''):
            return '%s' % input_data
        def gds_validate_boolean_list(self, input_data, node, input_name=''):
            values = input_data.split()
            for value in values:
                if value not in ('true', '1', 'false', '0', ):
                    raise_parse_error(node, 'Requires sequence of booleans ("true", "1", "false", "0")')
            return input_data
        def gds_str_lower(self, instring):
            return instring.lower()
        def get_path_(self, node):
            path_list = []
            self.get_path_list_(node, path_list)
            path_list.reverse()
            path = '/'.join(path_list)
            return path
        Tag_strip_pattern_ = re_.compile(r'\{.*\}')
        def get_path_list_(self, node, path_list):
            if node is None:
                return
            tag = GeneratedsSuper.Tag_strip_pattern_.sub('', node.tag)
            if tag:
                path_list.append(tag)
            self.get_path_list_(node.getparent(), path_list)
        def get_class_obj_(self, node, default_class=None):
            class_obj1 = default_class
            if 'xsi' in node.nsmap:
                classname = node.get('{%s}type' % node.nsmap['xsi'])
                if classname is not None:
                    names = classname.split(':')
                    if len(names) == 2:
                        classname = names[1]
                    class_obj2 = globals().get(classname)
                    if class_obj2 is not None:
                        class_obj1 = class_obj2
            return class_obj1
        def gds_build_any(self, node, type_name=None):
            return None


#
# If you have installed IPython you can uncomment and use the following.
# IPython is available from http://ipython.scipy.org/.
#

## from IPython.Shell import IPShellEmbed
## args = ''
## ipshell = IPShellEmbed(args,
##     banner = 'Dropping into IPython',
##     exit_msg = 'Leaving Interpreter, back to program.')

# Then use the following line where and when you want to drop into the
# IPython shell:
#    ipshell('<some message> -- Entering ipshell.\nHit Ctrl-D to exit')

#
# Globals
#

ExternalEncoding = 'ascii'
Tag_pattern_ = re_.compile(r'({.*})?(.*)')
String_cleanup_pat_ = re_.compile(r"[\n\r\s]+")
Namespace_extract_pat_ = re_.compile(r'{(.*)}(.*)')

#
# Support/utility functions.
#

def showIndent(outfile, level):
    for idx in range(level):
        outfile.write('    ')

def quote_xml(inStr):
    if not inStr:
        return ''
    s1 = (isinstance(inStr, basestring) and inStr or
          '%s' % inStr)
    s1 = s1.replace('&', '&amp;')
    s1 = s1.replace('<', '&lt;')
    s1 = s1.replace('>', '&gt;')
    return s1

def quote_attrib(inStr):
    s1 = (isinstance(inStr, basestring) and inStr or
          '%s' % inStr)
    s1 = s1.replace('&', '&amp;')
    s1 = s1.replace('<', '&lt;')
    s1 = s1.replace('>', '&gt;')
    if '"' in s1:
        if "'" in s1:
            s1 = '"%s"' % s1.replace('"', "&quot;")
        else:
            s1 = "'%s'" % s1
    else:
        s1 = '"%s"' % s1
    return s1

def quote_python(inStr):
    s1 = inStr
    if s1.find("'") == -1:
        if s1.find('\n') == -1:
            return "'%s'" % s1
        else:
            return "'''%s'''" % s1
    else:
        if s1.find('"') != -1:
            s1 = s1.replace('"', '\\"')
        if s1.find('\n') == -1:
            return '"%s"' % s1
        else:
            return '"""%s"""' % s1

def get_all_text_(node):
    if node.text is not None:
        text = node.text
    else:
        text = ''
    for child in node:
        if child.tail is not None:
            text += child.tail
    return text

def find_attr_value_(attr_name, node):
    attrs = node.attrib
    attr_parts = attr_name.split(':')
    value = None
    if len(attr_parts) == 1:
        value = attrs.get(attr_name)
    elif len(attr_parts) == 2:
        prefix, name = attr_parts
        namespace = node.nsmap.get(prefix)
        if namespace is not None:
            value = attrs.get('{%s}%s' % (namespace, name, ))
    return value


class GDSParseError(Exception):
    pass

def raise_parse_error(node, msg):
    if XMLParser_import_library == XMLParser_import_lxml:
        msg = '%s (element %s/line %d)' % (msg, node.tag, node.sourceline, )
    else:
        msg = '%s (element %s)' % (msg, node.tag, )
    raise GDSParseError(msg)


class MixedContainer:
    # Constants for category:
    CategoryNone = 0
    CategoryText = 1
    CategorySimple = 2
    CategoryComplex = 3
    # Constants for content_type:
    TypeNone = 0
    TypeText = 1
    TypeString = 2
    TypeInteger = 3
    TypeFloat = 4
    TypeDecimal = 5
    TypeDouble = 6
    TypeBoolean = 7
    def __init__(self, category, content_type, name, value):
        self.category = category
        self.content_type = content_type
        self.name = name
        self.value = value
    def getCategory(self):
        return self.category
    def getContenttype(self, content_type):
        return self.content_type
    def getValue(self):
        return self.value
    def getName(self):
        return self.name
    def export(self, outfile, level, name, namespace):
        if self.category == MixedContainer.CategoryText:
            # Prevent exporting empty content as empty lines.
            if self.value.strip(): 
                outfile.write(self.value)
        elif self.category == MixedContainer.CategorySimple:
            self.exportSimple(outfile, level, name)
        else:    # category == MixedContainer.CategoryComplex
            self.value.export(outfile, level, namespace,name)
    def exportSimple(self, outfile, level, name):
        if self.content_type == MixedContainer.TypeString:
            outfile.write('<%s>%s</%s>' % (self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeInteger or \
                self.content_type == MixedContainer.TypeBoolean:
            outfile.write('<%s>%d</%s>' % (self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeFloat or \
                self.content_type == MixedContainer.TypeDecimal:
            outfile.write('<%s>%f</%s>' % (self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeDouble:
            outfile.write('<%s>%g</%s>' % (self.name, self.value, self.name))
    def exportLiteral(self, outfile, level, name):
        if self.category == MixedContainer.CategoryText:
            showIndent(outfile, level)
            outfile.write('model_.MixedContainer(%d, %d, "%s", "%s"),\n' % \
                (self.category, self.content_type, self.name, self.value))
        elif self.category == MixedContainer.CategorySimple:
            showIndent(outfile, level)
            outfile.write('model_.MixedContainer(%d, %d, "%s", "%s"),\n' % \
                (self.category, self.content_type, self.name, self.value))
        else:    # category == MixedContainer.CategoryComplex
            showIndent(outfile, level)
            outfile.write('model_.MixedContainer(%d, %d, "%s",\n' % \
                (self.category, self.content_type, self.name,))
            self.value.exportLiteral(outfile, level + 1)
            showIndent(outfile, level)
            outfile.write(')\n')


class MemberSpec_(object):
    def __init__(self, name='', data_type='', container=0):
        self.name = name
        self.data_type = data_type
        self.container = container
    def set_name(self, name): self.name = name
    def get_name(self): return self.name
    def set_data_type(self, data_type): self.data_type = data_type
    def get_data_type_chain(self): return self.data_type
    def get_data_type(self):
        if isinstance(self.data_type, list):
            if len(self.data_type) > 0:
                return self.data_type[-1]
            else:
                return 'xs:string'
        else:
            return self.data_type
    def set_container(self, container): self.container = container
    def get_container(self): return self.container

def _cast(typ, value):
    if typ is None or value is None:
        return value
    return typ(value)

#
# Data representation classes.
#

class DiskPartitionObjectType(common.DefinedObjectType):
    """The DiskPartitionType type is intended to characterize partitions of
    disk drives."""
    subclass = None
    superclass = common.DefinedObjectType
    def __init__(self, Created=None, Device_Name=None, Mount_Point=None, Partition_ID=None, Partition_Length=None, Partition_Offset=None, Space_Left=None, Space_Used=None, Total_Space=None, Type=None):
        super(DiskPartitionObjectType, self).__init__(None)
        self.Created = Created
        self.Device_Name = Device_Name
        self.Mount_Point = Mount_Point
        self.Partition_ID = Partition_ID
        self.Partition_Length = Partition_Length
        self.Partition_Offset = Partition_Offset
        self.Space_Left = Space_Left
        self.Space_Used = Space_Used
        self.Total_Space = Total_Space
        self.Type = Type
    def factory(*args_, **kwargs_):
        if DiskPartitionObjectType.subclass:
            return DiskPartitionObjectType.subclass(*args_, **kwargs_)
        else:
            return DiskPartitionObjectType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Created(self): return self.Created
    def set_Created(self, Created): self.Created = Created
    def get_Device_Name(self): return self.Device_Name
    def set_Device_Name(self, Device_Name): self.Device_Name = Device_Name
    def get_Mount_Point(self): return self.Mount_Point
    def set_Mount_Point(self, Mount_Point): self.Mount_Point = Mount_Point
    def get_Partition_ID(self): return self.Partition_ID
    def set_Partition_ID(self, Partition_ID): self.Partition_ID = Partition_ID
    def get_Partition_Length(self): return self.Partition_Length
    def set_Partition_Length(self, Partition_Length): self.Partition_Length = Partition_Length
    def get_Partition_Offset(self): return self.Partition_Offset
    def set_Partition_Offset(self, Partition_Offset): self.Partition_Offset = Partition_Offset
    def get_Space_Left(self): return self.Space_Left
    def set_Space_Left(self, Space_Left): self.Space_Left = Space_Left
    def get_Space_Used(self): return self.Space_Used
    def set_Space_Used(self, Space_Used): self.Space_Used = Space_Used
    def get_Total_Space(self): return self.Total_Space
    def set_Total_Space(self, Total_Space): self.Total_Space = Total_Space
    def get_Type(self): return self.Type
    def set_Type(self, Type): self.Type = Type
    def validate_PartitionType(self, value):
        # Validate type PartitionType, a restriction on None.
        pass
    def export(self, outfile, level, namespace_='DiskPartitionObj:', name_='DiskPartitionObjectType', namespacedef_=''):
        showIndent(outfile, level)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='DiskPartitionObjectType')
        if self.hasContent_():
            outfile.write('>\n')
            self.exportChildren(outfile, level + 1, namespace_, name_)
            showIndent(outfile, level)
            outfile.write('</%s%s>\n' % (namespace_, name_))
        else:
            outfile.write('/>\n')
    def exportAttributes(self, outfile, level, already_processed, namespace_='DiskPartitionObj:', name_='DiskPartitionObjectType'):
        super(DiskPartitionObjectType, self).exportAttributes(outfile, level, already_processed, namespace_, name_='DiskPartitionObjectType')
    def exportChildren(self, outfile, level, namespace_='DiskPartitionObj:', name_='DiskPartitionObjectType', fromsubclass_=False):
        if self.Created is not None:
            self.Created.export(outfile, level, 'DiskPartitionObj:', name_='Created')
        if self.Device_Name is not None:
            self.Device_Name.export(outfile, level, 'DiskPartitionObj:', name_='Device_Name')
        if self.Mount_Point is not None:
            self.Mount_Point.export(outfile, level, 'DiskPartitionObj:', name_='Mount_Point')
        if self.Partition_ID is not None:
            self.Partition_ID.export(outfile, level, 'DiskPartitionObj:', name_='Partition_ID')
        if self.Partition_Length is not None:
            self.Partition_Length.export(outfile, level, 'DiskPartitionObj:', name_='Partition_Length')
        if self.Partition_Offset is not None:
            self.Partition_Offset.export(outfile, level, 'DiskPartitionObj:', name_='Partition_Offset')
        if self.Space_Left is not None:
            self.Space_Left.export(outfile, level, 'DiskPartitionObj:', name_='Space_Left')
        if self.Space_Used is not None:
            self.Space_Used.export(outfile, level, 'DiskPartitionObj:', name_='Space_Used')
        if self.Total_Space is not None:
            self.Total_Space.export(outfile, level, 'DiskPartitionObj:', name_='Total_Space')
        if self.Type is not None:
            self.Type.export(outfile, level, 'DiskPartitionObj:', name_='Type')
    def hasContent_(self):
        if (
            self.Created is not None or
            self.Device_Name is not None or
            self.Mount_Point is not None or
            self.Partition_ID is not None or
            self.Partition_Length is not None or
            self.Partition_Offset is not None or
            self.Space_Left is not None or
            self.Space_Used is not None or
            self.Total_Space is not None or
            self.Type is not None
            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='DiskPartitionObjectType'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        if self.Created is not None:
            showIndent(outfile, level)
            outfile.write('Created=%s,\n' % quote_python(self.Created).encode(ExternalEncoding))
        if self.Device_Name is not None:
            showIndent(outfile, level)
            outfile.write('Device_Name=%s,\n' % quote_python(self.Device_Name).encode(ExternalEncoding))
        if self.Mount_Point is not None:
            showIndent(outfile, level)
            outfile.write('Mount_Point=%s,\n' % quote_python(self.Mount_Point).encode(ExternalEncoding))
        if self.Partition_ID is not None:
            showIndent(outfile, level)
            outfile.write('Partition_ID=%s,\n' % quote_python(self.Partition_ID).encode(ExternalEncoding))
        if self.Partition_Length is not None:
            showIndent(outfile, level)
            outfile.write('Partition_Length=%s,\n' % quote_python(self.Partition_Length).encode(ExternalEncoding))
        if self.Partition_Offset is not None:
            showIndent(outfile, level)
            outfile.write('Partition_Offset=%s,\n' % quote_python(self.Partition_Offset).encode(ExternalEncoding))
        if self.Space_Left is not None:
            showIndent(outfile, level)
            outfile.write('Space_Left=%s,\n' % quote_python(self.Space_Left).encode(ExternalEncoding))
        if self.Space_Used is not None:
            showIndent(outfile, level)
            outfile.write('Space_Used=%s,\n' % quote_python(self.Space_Used).encode(ExternalEncoding))
        if self.Total_Space is not None:
            showIndent(outfile, level)
            outfile.write('Total_Space=%s,\n' % quote_python(self.Total_Space).encode(ExternalEncoding))
        if self.Type is not None:
            showIndent(outfile, level)
            outfile.write('Type=model_.PartitionType(\n')
            self.Type.exportLiteral(outfile, level, name_='Type')
            showIndent(outfile, level)
            outfile.write('),\n')
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Created':
            Created_ = child_.text
            Created_ = self.gds_validate_string(Created_, node, 'Created')
            self.Created = Created_
        elif nodeName_ == 'Device_Name':
            Device_Name_ = child_.text
            Device_Name_ = self.gds_validate_string(Device_Name_, node, 'Device_Name')
            self.Device_Name = Device_Name_
        elif nodeName_ == 'Mount_Point':
            Mount_Point_ = child_.text
            Mount_Point_ = self.gds_validate_string(Mount_Point_, node, 'Mount_Point')
            self.Mount_Point = Mount_Point_
        elif nodeName_ == 'Partition_ID':
            Partition_ID_ = child_.text
            Partition_ID_ = self.gds_validate_string(Partition_ID_, node, 'Partition_ID')
            self.Partition_ID = Partition_ID_
        elif nodeName_ == 'Partition_Length':
            Partition_Length_ = child_.text
            Partition_Length_ = self.gds_validate_string(Partition_Length_, node, 'Partition_Length')
            self.Partition_Length = Partition_Length_
        elif nodeName_ == 'Partition_Offset':
            Partition_Offset_ = child_.text
            Partition_Offset_ = self.gds_validate_string(Partition_Offset_, node, 'Partition_Offset')
            self.Partition_Offset = Partition_Offset_
        elif nodeName_ == 'Space_Left':
            Space_Left_ = child_.text
            Space_Left_ = self.gds_validate_string(Space_Left_, node, 'Space_Left')
            self.Space_Left = Space_Left_
        elif nodeName_ == 'Space_Used':
            Space_Used_ = child_.text
            Space_Used_ = self.gds_validate_string(Space_Used_, node, 'Space_Used')
            self.Space_Used = Space_Used_
        elif nodeName_ == 'Total_Space':
            Total_Space_ = child_.text
            Total_Space_ = self.gds_validate_string(Total_Space_, node, 'Total_Space')
            self.Total_Space = Total_Space_
        elif nodeName_ == 'Type':
            obj_ = None
            self.set_Type(obj_)
            self.validate_PartitionType(self.Type)    # validate type PartitionType
        super(DiskPartitionObjectType, self).buildChildren(child_, node, nodeName_, True)
# end class DiskPartitionObjectType


class PartitionType(GeneratedsSuper):
    """PartitionType specifies partition types, via a union of the
    PartitionTypeEnum type and the atomic xs:string type. Its base
    type is the CybOX Core BaseObjectAttributeType, for permitting
    complex (i.e. regular-expression based) specifications.This
    attribute is optional and specifies the expected type for the
    value of the specified element."""
    subclass = None
    superclass = None
    def __init__(self, datatype=None, valueOf_=None):
        self.datatype = _cast(None, datatype)
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if PartitionType.subclass:
            return PartitionType.subclass(*args_, **kwargs_)
        else:
            return PartitionType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_datatype(self): return self.datatype
    def set_datatype(self, datatype): self.datatype = datatype
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def export(self, outfile, level, namespace_='DiskPartitionObj:', name_='PartitionType', namespacedef_=''):
        showIndent(outfile, level)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='PartitionType')
        if self.hasContent_():
            outfile.write('>')
            outfile.write(str(self.valueOf_).encode(ExternalEncoding))
            self.exportChildren(outfile, level + 1, namespace_, name_)
            outfile.write('</%s%s>\n' % (namespace_, name_))
        else:
            outfile.write('/>\n')
    def exportAttributes(self, outfile, level, already_processed, namespace_='DiskPartitionObj:', name_='PartitionType'):
        if self.datatype is not None and 'datatype' not in already_processed:
            already_processed.append('datatype')
            outfile.write(' datatype=%s' % (quote_attrib(self.datatype), ))
    def exportChildren(self, outfile, level, namespace_='DiskPartitionObj:', name_='PartitionType', fromsubclass_=False):
        pass
    def hasContent_(self):
        if (
            self.valueOf_
            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='PartitionType'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
        showIndent(outfile, level)
        outfile.write('valueOf_ = """%s""",\n' % (self.valueOf_,))
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        if self.datatype is not None and 'datatype' not in already_processed:
            already_processed.append('datatype')
            showIndent(outfile, level)
            outfile.write('datatype = %s,\n' % (self.datatype,))
    def exportLiteralChildren(self, outfile, level, name_):
        pass
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        self.valueOf_ = get_all_text_(node)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('datatype', node)
        if value is not None and 'datatype' not in already_processed:
            already_processed.append('datatype')
            self.datatype = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class PartitionType


USAGE_TEXT = """
Usage: python <Parser>.py [ -s ] <in_xml_file>
"""

def usage():
    print USAGE_TEXT
    sys.exit(1)


def get_root_tag(node):
    tag = Tag_pattern_.match(node.tag).groups()[-1]
    rootClass = globals().get(tag)
    return tag, rootClass


def parse(inFileName):
    doc = parsexml_(inFileName)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'Disk_Partition'
        rootClass = DiskPartitionObjectType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    sys.stdout.write('<?xml version="1.0" ?>\n')
    rootObj.export(sys.stdout, 0, name_=rootTag, 
        namespacedef_='')
    return rootObj


def parseString(inString):
    from StringIO import StringIO
    doc = parsexml_(StringIO(inString))
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'Disk_Partition'
        rootClass = DiskPartitionObjectType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    sys.stdout.write('<?xml version="1.0" ?>\n')
    rootObj.export(sys.stdout, 0, name_="Disk_Partition",
        namespacedef_='')
    return rootObj


def parseLiteral(inFileName):
    doc = parsexml_(inFileName)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'Disk_Partition'
        rootClass = DiskPartitionObjectType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    sys.stdout.write('#from Disk_Partition_Object import *\n\n')
    sys.stdout.write('import Disk_Partition_Object as model_\n\n')
    sys.stdout.write('rootObj = model_.rootTag(\n')
    rootObj.exportLiteral(sys.stdout, 0, name_=rootTag)
    sys.stdout.write(')\n')
    return rootObj


def main():
    args = sys.argv[1:]
    if len(args) == 1:
        parse(args[0])
    else:
        usage()


if __name__ == '__main__':
    #import pdb; pdb.set_trace()
    main()


__all__ = [
    "DiskPartitionObjectType",
    "PartitionType"
    ]
