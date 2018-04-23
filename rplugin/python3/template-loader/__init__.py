# -*- coding: utf-8 -*-

import os.path
import datetime

import neovim


cpp_head_temp = '#ifndef {0}\n#define {0}\n\n\n#endif // {0}'


@neovim.plugin
class TemplatePlugin:

    def __init__(self, nvim):
        self.nvim = nvim

    @neovim.autocmd('BufNewfile', pattern='*.h,*.hpp')
    def loadTemplate(self):
        filename = self.nvim.current.buffer.name
        filename = os.path.basename(filename).upper().replace('.', '_')

        date = str(datetime.date.today()).replace('-', '')

        define_str = filename + '_' + date
        temp_str = cpp_head_temp.format(define_str)

        for line in temp_str.split('\n'):
            self.nvim.current.buffer.append(line)
