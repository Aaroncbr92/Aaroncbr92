#!/bin/bash
# Vuelca, con la redacción vigente hoy, las normas del temario común de Canal Sur.
# Salta las ya volcadas, para poder relanzarlo.
cd "$(dirname "$0")/../.."
for id in BOE-A-1978-31229 BOE-A-1985-5392 BOE-A-2010-11491 BOE-A-2007-5825 BOE-A-2006-20848 \
  BOE-A-2007-19819 BOE-A-2024-16885 BOE-A-1984-1847 BOE-A-1988-8592 BOE-A-2021-11380 \
  BOE-A-2022-11311 BOE-A-2018-15240 BOE-A-2008-1185 BOE-A-2005-655 BOE-A-2008-2492 \
  BOE-A-2022-11589 BOE-A-2023-5366 BOE-A-1995-24292 BOE-A-2018-16673 BOE-A-1982-11196 \
  BOE-A-1984-7248; do
  [ -s fuentes/canal-sur/$id.md ] && { echo "ya: $id"; continue; }
  for i in 1 2 3; do timeout 900 python3 herramientas/boe.py norma $id fuentes/canal-sur/ && break; sleep $((i*5)); done
done
