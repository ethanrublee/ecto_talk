fname = 'contact.txt'
hl = [(_('(IRC:|MAILINGLIST:|WWW:|CODE:)+', green, bold),
       _('(http:[^\s]+|irc.*)+', yellow),
       )
      ]
