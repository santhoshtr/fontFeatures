import copy

def shaper_inputs(self):
    return self.input


def _do_apply(self, buf, ix):
    from fontFeatures.jankyPOS.Buffer import BufferItem

    coverage = buf[ix : ix + len(self.input)]
    newstuff = []
    # Handle single subst first
    if len(self.input) == 1 and len(self.replacement) == 1:
        buf[ix].glyph = self.replacement[0][self.input[0].index(buf[ix].glyph)]
        buf[ix].prep_glyph(buf.font)
        return

    for g in self.replacement:
        new_glyph = copy.copy(buf[ix])
        new_glyph.glyph = g[0]
        new_glyph.prep_glyph(buf.font)
        print(g[0], new_glyph.position.asFea())
        newstuff.append(new_glyph)
    buf[ix : ix + len(self.input)] = newstuff