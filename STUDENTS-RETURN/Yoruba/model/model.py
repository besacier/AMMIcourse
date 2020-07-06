# @Author: Ibrahim Salihu Yusuf <yusuf>
# @Date:   2020-07-06T19:32:07+02:00
# @Email:  sibrahim1396@gmail.com
# @Last modified by:   yusuf
# @Last modified time: 2020-07-06T19:33:46+02:00
import torch
import torch.nn as nn

class CPCModel(nn.Module):
    def __init__(self,
                 encoder,
                 AR):

        super(CPCModel, self).__init__()
        self.gEncoder = encoder
        self.gAR = AR

    def forward(self, batch_data, label=None):
        encoder_output = self.gEncoder(batch_data).permute(0, 2, 1)
        context_output = self.gAR(encoder_output)
        return context_output, encoder_output, label
