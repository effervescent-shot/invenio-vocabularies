# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 CERN.
#
# Invenio-Vocabularies is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""Vocabulary facets."""

from .facets import NestedVocabularyTermsFacet
from .labels import VocabularyLabels

__all__ = (
    "NestedVocabularyTermsFacet",
    "VocabularyLabels",
)
