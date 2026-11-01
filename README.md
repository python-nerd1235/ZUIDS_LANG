# ZUIDS_LANG
Just a stupid thing   :)

# how it works
In a ZISC, the code can not change. You set the data. In ZUIDS_LANG, you set the code, the data is constant.

If you ran offset 4,
this:
      
      list : [0,1,2..., 254, 255]
      index:  0 1 2...  254  255

            |
            V

      list : [0,1,2..., 254, 255]
      index:255 0 1...  253  254
is now this!

# commads

      offset x

        set the offset to x

      ExpOffset x

        Evaluate x and that is the new offset

      if x

        if x, go back 5 lines

!NOP

  NO OP

# "_" staments

_OFF

  Returns the current offset

_IN

  Returns user input

_OFFDAT

  Returns the data at the current offset


HAVE FUN! 
:)
