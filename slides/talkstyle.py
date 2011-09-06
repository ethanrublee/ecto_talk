# -*- coding: utf-8 -*-
"""
    pygments.styles.fruity
    ~~~~~~~~~~~~~~~~~~~~~~

    pygments version of my "fruity" vim theme.

    :copyright: Copyright 2006-2010 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""

from pygments.style import Style
from pygments.token import Token, Comment, Name, Keyword, \
    Generic, Number, String, Whitespace, Other, Operator

class TalkStyle(Style):
    """
    Pygments version of the "native" vim theme.
    """

    background_color = '#111111'
    highlight_color = '#333333'

    styles = {
        Other:              '#ff2222 bold',
        #Whitespace:         '#888888',
        Token:              '#dddddd',
        Operator:           '#ffffcc',
        #Generic.Output:     '#444444 bg:#222222',
        #Keyword:            '#fb664a',
        #Keyword.Pseudo:     'nobold',
        #Number:             '#7086f7',
        #Name.Tag:           '#fb660a',
        #Name.Variable:      '#fb660a',
        #Name.Constant:      '#fb660a',
        # Comment:            '#008800 bg:#0f140f italic',
#         Name.Attribute:     '#ff0086',
#         String:             '#ff86d2',
#         Name.Function:      '#ff0086',
#         Generic.Heading:    '#ffffff',
#         Keyword.Type:       '#cdcaa9',
#         Generic.Subheading: '#ffffff',
#         Name.Constant:      '#0086d2',
#         Comment.Preproc:    '#ff0007'
    }
