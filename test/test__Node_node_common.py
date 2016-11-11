#!/usr/bin/env python
#-*-coding:utf-8-*-
'''
@author: hualingson
@license: gpl
'''

from common.node import Node

root = Node('root')
sub_a = Node('sub_a', 1)
sub_b = Node('sub_b', 1)
grand_a = Node('grand_a', 2)
grand_b = Node('grand_b', 2)
grand_c = Node('grand_c', 2)
grand_d = Node('grand_d', 2)
grand_e = Node('grand_e', 2)
leaf_a = Node('leaf_a', 3)
leaf_b = Node('leaf_b', 3)

root.SetAttribute('sex', 'unknown')
root.SetAttribute('age', 'infinite')
sub_a.SetAttribute('sex', 'male')
sub_a.SetAttribute('age', 'elder than 10000')
sub_b.SetAttribute('sex', 'female')
sub_b.SetAttribute('age', 'elder than 9000')
grand_a.SetAttribute('sex', 'male')
grand_a.SetAttribute('age', 'about 5000')
grand_b.SetAttribute('sex', 'female')
grand_b.SetAttribute('age', 'about 4000')
grand_c.SetAttribute('sex', 'female')
grand_c.SetAttribute('age', 'about 4800')
grand_d.SetAttribute('sex', 'male')
grand_d.SetAttribute('age', 'about 4500')
grand_e.SetAttribute('sex', 'female')
grand_e.SetAttribute('age', 'about 4200')
leaf_a.SetAttribute('hasgirlfriend', 'yes')
leaf_a.SetAttribute('iscoder', 'no')
leaf_b.SetAttribute('hasgirlfriend', 'no')
leaf_b.SetAttribute('iscoder', 'yes')

root.AppendKid(sub_a)
root.AppendKid(sub_b)
sub_a.AppendKid(grand_a)
sub_a.AppendKid(grand_b)
sub_a.AppendKid(grand_c)
sub_a.AppendKid(grand_d)
sub_b.AppendKid(grand_e)
grand_e.AppendKid(leaf_a)
grand_e.AppendKid(leaf_b)

print root
'''

<root age="infinite" sex="unknown">
    <sub_a age="elder than 10000" sex="male">
        <grand_a age="about 5000" sex="male" />
        <grand_b age="about 4000" sex="female" />
        <grand_c age="about 4800" sex="female" />
        <grand_d age="about 4500" sex="male" />
    </sub_a>
    <sub_b age="elder than 9000" sex="female">
        <grand_e age="about 4200" sex="female">
            <leaf_a iscoder="no" hasgirlfriend="yes" />
            <leaf_b iscoder="yes" hasgirlfriend="no" />
        </grand_e>
    </sub_b>
</root>
'''
