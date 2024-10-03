# ckm_image_processing

Description.

The package package_name is used to:

Processing:

- Histogram matching
- Structural similarity
- Resize image

Utils:

- Read image
- Save image

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install ckm_image_processing

```bash
pip install ckm_image_processing
```

## Usage

```python
from ckm_image_processing.utils import io, plot
from ckm_image_processing.processing import combination, transformation

image1 = io.read_image('path do arquivo imagem')
image2 = io.read_image('path do arquivo imagem')

plot.plot_image(image1)
plot.plot_image(image2)

result_image = combination.transfer_histogram(image1, image2)
plot.plot_result(image1, image2, result_image)
```

## Author

Celso Mihara
