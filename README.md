# generalisePrometheusMetrics
Generalise Prometheus metrics. 
removes instance specific attributes, replaces variables. makes it easier to copy from Prometheus console straight to Grafana.

For example:
original metrics -
```
gauge{_label_0="hello", _label_1="joe", _label_2="biden", domain="america_com", env="production", envName="qa-joe-biden-1", instance="99.999.99.999:42069", kitVersion="joe-biden-1.0", namespace="presidents", pod="joe-biden-1",}
```

output -
```
gauge{_label_0="hello", _label_1="joe", _label_2="biden", domain="america_com", env="production", envName="~$envName", namespace="presidents", }
```
