# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree.
#
# Llama 2 is licensed under the LLAMA 2 Community License,
# Copyright (c) Meta Platforms, Inc. All Rights Reserved.

from torchtitan.models.llama.model import ModelArgs, Transformer
from torchtitan.models.llama.diffusion_model import DiffusionTransformer, DiffusionModelArgs

__all__ = ["Transformer", "DiffusionTransformer"]

llama2_configs = {
    "debugmodel": ModelArgs(dim=256, n_layers=8, n_heads=16),
    "271M": ModelArgs(dim=1024, n_layers=16, n_heads=8),
    "1B": ModelArgs(dim=2048, n_layers=18, n_heads=16),
    "7B": ModelArgs(dim=4096, n_layers=32, n_heads=32),
    "13B": ModelArgs(dim=5120, n_layers=40, n_heads=40),
    "26B": ModelArgs(dim=5120, n_layers=80, n_heads=40),
    "70B": ModelArgs(
        dim=8192,
        n_layers=80,
        n_heads=64,
        n_kv_heads=8,
        ffn_dim_multiplier=1.3,
        multiple_of=4096,
    ),
}

llama3_configs = {
    "debugmodel": ModelArgs(dim=256, n_layers=8, n_heads=16, rope_theta=500000),
    "8B": ModelArgs(
        dim=4096,
        n_layers=32,
        n_heads=32,
        n_kv_heads=8,
        ffn_dim_multiplier=1.3,
        multiple_of=1024,
        rope_theta=500000,
    ),
    "70B": ModelArgs(
        dim=8192,
        n_layers=80,
        n_heads=64,
        n_kv_heads=8,
        ffn_dim_multiplier=1.3,
        multiple_of=4096,
        rope_theta=500000,
    ),
    "405B": ModelArgs(
        dim=16384,
        n_layers=126,
        n_heads=128,
        n_kv_heads=8,
        ffn_dim_multiplier=1.2,
        multiple_of=4096,
        rope_theta=500000,
    ),
}

llama3_diffusion_configs = {
    "debugmodel": DiffusionModelArgs(dim=256, n_layers=8, n_heads=16, rope_theta=10000, patch_size=2),
    "DiT-S": DiffusionModelArgs(dim=384, n_layers=12, n_heads=8, rope_theta=10000),
    "DiT-L": DiffusionModelArgs(dim=1024, n_layers=24, n_heads=16, rope_theta=10000),
    "DiT-1B": DiffusionModelArgs(dim=1536, n_layers=32, n_heads=32, rope_theta=10000), #around 1.5 B actually
    "DiT-7B": DiffusionModelArgs(dim=2560, n_layers=60, n_heads=64, rope_theta=10000),
}
