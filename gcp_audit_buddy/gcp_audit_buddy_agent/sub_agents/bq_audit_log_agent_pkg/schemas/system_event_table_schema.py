SYSTEM_EVENT_TABLE_SCHEMA = """[
  {
    "mode": "NULLABLE",
    "name": "logName",
    "type": "STRING"
  },
  {
    "fields": [
      {
        "mode": "NULLABLE",
        "name": "type",
        "type": "STRING"
      },
      {
        "fields": [
          {
            "mode": "NULLABLE",
            "name": "project_id",
            "type": "STRING"
          },
          {
            "mode": "NULLABLE",
            "name": "zone",
            "type": "STRING"
          },
          {
            "mode": "NULLABLE",
            "name": "instance_id",
            "type": "STRING"
          }
        ],
        "mode": "NULLABLE",
        "name": "labels",
        "type": "RECORD"
      }
    ],
    "mode": "NULLABLE",
    "name": "resource",
    "type": "RECORD"
  },
  {
    "fields": [
      {
        "mode": "NULLABLE",
        "name": "serviceName",
        "type": "STRING"
      },
      {
        "mode": "NULLABLE",
        "name": "methodName",
        "type": "STRING"
      },
      {
        "mode": "NULLABLE",
        "name": "resourceName",
        "type": "STRING"
      },
      {
        "fields": [
          {
            "mode": "REPEATED",
            "name": "currentLocations",
            "type": "STRING"
          },
          {
            "mode": "REPEATED",
            "name": "originalLocations",
            "type": "STRING"
          }
        ],
        "mode": "NULLABLE",
        "name": "resourceLocation",
        "type": "RECORD"
      },
      {
        "mode": "NULLABLE",
        "name": "numResponseItems",
        "type": "INTEGER"
      },
      {
        "fields": [
          {
            "mode": "NULLABLE",
            "name": "code",
            "type": "INTEGER"
          },
          {
            "mode": "NULLABLE",
            "name": "message",
            "type": "STRING"
          }
        ],
        "mode": "NULLABLE",
        "name": "status",
        "type": "RECORD"
      },
      {
        "fields": [
          {
            "mode": "NULLABLE",
            "name": "principalEmail",
            "type": "STRING"
          },
          {
            "mode": "NULLABLE",
            "name": "authoritySelector",
            "type": "STRING"
          },
          {
            "mode": "NULLABLE",
            "name": "serviceAccountKeyName",
            "type": "STRING"
          },
          {
            "fields": [
              {
                "mode": "NULLABLE",
                "name": "principalSubject",
                "type": "STRING"
              },
              {
                "fields": [
                  {
                    "mode": "NULLABLE",
                    "name": "principalEmail",
                    "type": "STRING"
                  }
                ],
                "mode": "NULLABLE",
                "name": "firstPartyPrincipal",
                "type": "RECORD"
              }
            ],
            "mode": "REPEATED",
            "name": "serviceAccountDelegationInfo",
            "type": "RECORD"
          },
          {
            "mode": "NULLABLE",
            "name": "principalSubject",
            "type": "STRING"
          },
          {
            "fields": [
              {
                "mode": "NULLABLE",
                "name": "originalPrincipal",
                "type": "STRING"
              },
              {
                "fields": [
                  {
                    "mode": "NULLABLE",
                    "name": "principalSubject",
                    "type": "STRING"
                  },
                  {
                    "mode": "NULLABLE",
                    "name": "serviceDomain",
                    "type": "STRING"
                  }
                ],
                "mode": "REPEATED",
                "name": "serviceMetadata",
                "type": "RECORD"
              }
            ],
            "mode": "NULLABLE",
            "name": "serviceDelegationHistory",
            "type": "RECORD"
          }
        ],
        "mode": "NULLABLE",
        "name": "authenticationInfo",
        "type": "RECORD"
      },
      {
        "fields": [
          {
            "mode": "NULLABLE",
            "name": "resource",
            "type": "STRING"
          },
          {
            "mode": "NULLABLE",
            "name": "permission",
            "type": "STRING"
          },
          {
            "mode": "NULLABLE",
            "name": "granted",
            "type": "BOOLEAN"
          },
          {
            "fields": [
              {
                "mode": "NULLABLE",
                "name": "service",
                "type": "STRING"
              },
              {
                "mode": "NULLABLE",
                "name": "name",
                "type": "STRING"
              },
              {
                "mode": "NULLABLE",
                "name": "type",
                "type": "STRING"
              },
              {
                "fields": [
                  {
                    "mode": "NULLABLE",
                    "name": "key",
                    "type": "STRING"
                  },
                  {
                    "mode": "NULLABLE",
                    "name": "value",
                    "type": "STRING"
                  }
                ],
                "mode": "REPEATED",
                "name": "labels",
                "type": "RECORD"
              },
              {
                "mode": "NULLABLE",
                "name": "uid",
                "type": "STRING"
              },
              {
                "fields": [
                  {
                    "mode": "NULLABLE",
                    "name": "key",
                    "type": "STRING"
                  },
                  {
                    "mode": "NULLABLE",
                    "name": "value",
                    "type": "STRING"
                  }
                ],
                "mode": "REPEATED",
                "name": "annotations",
                "type": "RECORD"
              },
              {
                "mode": "NULLABLE",
                "name": "displayName",
                "type": "STRING"
              },
              {
                "mode": "NULLABLE",
                "name": "createTime",
                "type": "TIMESTAMP"
              },
              {
                "mode": "NULLABLE",
                "name": "updateTime",
                "type": "TIMESTAMP"
              },
              {
                "mode": "NULLABLE",
                "name": "deleteTime",
                "type": "TIMESTAMP"
              },
              {
                "mode": "NULLABLE",
                "name": "etag",
                "type": "STRING"
              },
              {
                "mode": "NULLABLE",
                "name": "location",
                "type": "STRING"
              }
            ],
            "mode": "NULLABLE",
            "name": "resourceAttributes",
            "type": "RECORD"
          },
          {
            "mode": "NULLABLE",
            "name": "permissionType",
            "type": "STRING"
          }
        ],
        "mode": "REPEATED",
        "name": "authorizationInfo",
        "type": "RECORD"
      },
      {
        "fields": [
          {
            "fields": [
              {
                "mode": "NULLABLE",
                "name": "resourceType",
                "type": "STRING"
              },
              {
                "fields": [
                  {
                    "mode": "NULLABLE",
                    "name": "key",
                    "type": "STRING"
                  },
                  {
                    "mode": "NULLABLE",
                    "name": "value",
                    "type": "STRING"
                  }
                ],
                "mode": "REPEATED",
                "name": "resourceTags",
                "type": "RECORD"
              },
              {
                "fields": [
                  {
                    "mode": "NULLABLE",
                    "name": "constraint",
                    "type": "STRING"
                  },
                  {
                    "mode": "NULLABLE",
                    "name": "errorMessage",
                    "type": "STRING"
                  },
                  {
                    "mode": "NULLABLE",
                    "name": "checkedValue",
                    "type": "STRING"
                  },
                  {
                    "mode": "NULLABLE",
                    "name": "policyType",
                    "type": "STRING"
                  }
                ],
                "mode": "REPEATED",
                "name": "violationInfo",
                "type": "RECORD"
              }
            ],
            "mode": "NULLABLE",
            "name": "orgPolicyViolationInfo",
            "type": "RECORD"
          }
        ],
        "mode": "NULLABLE",
        "name": "policyViolationInfo",
        "type": "RECORD"
      },
      {
        "fields": [
          {
            "mode": "NULLABLE",
            "name": "callerIp",
            "type": "STRING"
          },
          {
            "mode": "NULLABLE",
            "name": "callerSuppliedUserAgent",
            "type": "STRING"
          },
          {
            "mode": "NULLABLE",
            "name": "callerNetwork",
            "type": "STRING"
          },
          {
            "fields": [
              {
                "mode": "NULLABLE",
                "name": "id",
                "type": "STRING"
              },
              {
                "mode": "NULLABLE",
                "name": "method",
                "type": "STRING"
              },
              {
                "fields": [
                  {
                    "mode": "NULLABLE",
                    "name": "key",
                    "type": "STRING"
                  },
                  {
                    "mode": "NULLABLE",
                    "name": "value",
                    "type": "STRING"
                  }
                ],
                "mode": "REPEATED",
                "name": "headers",
                "type": "RECORD"
              },
              {
                "mode": "NULLABLE",
                "name": "path",
                "type": "STRING"
              },
              {
                "mode": "NULLABLE",
                "name": "host",
                "type": "STRING"
              },
              {
                "mode": "NULLABLE",
                "name": "scheme",
                "type": "STRING"
              },
              {
                "mode": "NULLABLE",
                "name": "query",
                "type": "STRING"
              },
              {
                "mode": "NULLABLE",
                "name": "time",
                "type": "TIMESTAMP"
              },
              {
                "mode": "NULLABLE",
                "name": "size",
                "type": "INTEGER"
              },
              {
                "mode": "NULLABLE",
                "name": "protocol",
                "type": "STRING"
              },
              {
                "mode": "NULLABLE",
                "name": "reason",
                "type": "STRING"
              },
              {
                "fields": [
                  {
                    "mode": "NULLABLE",
                    "name": "principal",
                    "type": "STRING"
                  },
                  {
                    "mode": "REPEATED",
                    "name": "audiences",
                    "type": "STRING"
                  },
                  {
                    "mode": "NULLABLE",
                    "name": "presenter",
                    "type": "STRING"
                  },
                  {
                    "mode": "REPEATED",
                    "name": "accessLevels",
                    "type": "STRING"
                  }
                ],
                "mode": "NULLABLE",
                "name": "auth",
                "type": "RECORD"
              },
              {
                "mode": "NULLABLE",
                "name": "origin",
                "type": "STRING"
              }
            ],
            "mode": "NULLABLE",
            "name": "requestAttributes",
            "type": "RECORD"
          },
          {
            "fields": [
              {
                "mode": "NULLABLE",
                "name": "ip",
                "type": "STRING"
              },
              {
                "mode": "NULLABLE",
                "name": "port",
                "type": "INTEGER"
              },
              {
                "fields": [
                  {
                    "mode": "NULLABLE",
                    "name": "key",
                    "type": "STRING"
                  },
                  {
                    "mode": "NULLABLE",
                    "name": "value",
                    "type": "STRING"
                  }
                ],
                "mode": "REPEATED",
                "name": "labels",
                "type": "RECORD"
              },
              {
                "mode": "NULLABLE",
                "name": "principal",
                "type": "STRING"
              },
              {
                "mode": "NULLABLE",
                "name": "regionCode",
                "type": "STRING"
              }
            ],
            "mode": "NULLABLE",
            "name": "destinationAttributes",
            "type": "RECORD"
          }
        ],
        "mode": "NULLABLE",
        "name": "requestMetadata",
        "type": "RECORD"
      },
      {
        "mode": "NULLABLE",
        "name": "requestJson",
        "type": "STRING"
      },
      {
        "mode": "NULLABLE",
        "name": "responseJson",
        "type": "STRING"
      }
    ],
    "mode": "NULLABLE",
    "name": "protopayload_auditlog",
    "type": "RECORD"
  },
  {
    "mode": "NULLABLE",
    "name": "textPayload",
    "type": "STRING"
  },
  {
    "mode": "NULLABLE",
    "name": "timestamp",
    "type": "TIMESTAMP"
  },
  {
    "mode": "NULLABLE",
    "name": "receiveTimestamp",
    "type": "TIMESTAMP"
  },
  {
    "mode": "NULLABLE",
    "name": "severity",
    "type": "STRING"
  },
  {
    "mode": "NULLABLE",
    "name": "insertId",
    "type": "STRING"
  },
  {
    "fields": [
      {
        "mode": "NULLABLE",
        "name": "requestMethod",
        "type": "STRING"
      },
      {
        "mode": "NULLABLE",
        "name": "requestUrl",
        "type": "STRING"
      },
      {
        "mode": "NULLABLE",
        "name": "requestSize",
        "type": "INTEGER"
      },
      {
        "mode": "NULLABLE",
        "name": "status",
        "type": "INTEGER"
      },
      {
        "mode": "NULLABLE",
        "name": "responseSize",
        "type": "INTEGER"
      },
      {
        "mode": "NULLABLE",
        "name": "userAgent",
        "type": "STRING"
      },
      {
        "mode": "NULLABLE",
        "name": "remoteIp",
        "type": "STRING"
      },
      {
        "mode": "NULLABLE",
        "name": "serverIp",
        "type": "STRING"
      },
      {
        "mode": "NULLABLE",
        "name": "referer",
        "type": "STRING"
      },
      {
        "mode": "NULLABLE",
        "name": "cacheLookup",
        "type": "BOOLEAN"
      },
      {
        "mode": "NULLABLE",
        "name": "cacheHit",
        "type": "BOOLEAN"
      },
      {
        "mode": "NULLABLE",
        "name": "cacheValidatedWithOriginServer",
        "type": "BOOLEAN"
      },
      {
        "mode": "NULLABLE",
        "name": "cacheFillBytes",
        "type": "INTEGER"
      },
      {
        "mode": "NULLABLE",
        "name": "protocol",
        "type": "STRING"
      }
    ],
    "mode": "NULLABLE",
    "name": "httpRequest",
    "type": "RECORD"
  },
  {
    "fields": [
      {
        "mode": "NULLABLE",
        "name": "compute_googleapis_com_root_trigger_id",
        "type": "STRING"
      }
    ],
    "mode": "NULLABLE",
    "name": "labels",
    "type": "RECORD"
  },
  {
    "fields": [
      {
        "mode": "NULLABLE",
        "name": "id",
        "type": "STRING"
      },
      {
        "mode": "NULLABLE",
        "name": "producer",
        "type": "STRING"
      },
      {
        "mode": "NULLABLE",
        "name": "first",
        "type": "BOOLEAN"
      },
      {
        "mode": "NULLABLE",
        "name": "last",
        "type": "BOOLEAN"
      }
    ],
    "mode": "NULLABLE",
    "name": "operation",
    "type": "RECORD"
  },
  {
    "mode": "NULLABLE",
    "name": "trace",
    "type": "STRING"
  },
  {
    "mode": "NULLABLE",
    "name": "spanId",
    "type": "STRING"
  },
  {
    "mode": "NULLABLE",
    "name": "traceSampled",
    "type": "BOOLEAN"
  },
  {
    "fields": [
      {
        "mode": "NULLABLE",
        "name": "file",
        "type": "STRING"
      },
      {
        "mode": "NULLABLE",
        "name": "line",
        "type": "INTEGER"
      },
      {
        "mode": "NULLABLE",
        "name": "function",
        "type": "STRING"
      }
    ],
    "mode": "NULLABLE",
    "name": "sourceLocation",
    "type": "RECORD"
  },
  {
    "fields": [
      {
        "mode": "NULLABLE",
        "name": "uid",
        "type": "STRING"
      },
      {
        "mode": "NULLABLE",
        "name": "index",
        "type": "INTEGER"
      },
      {
        "mode": "NULLABLE",
        "name": "totalSplits",
        "type": "INTEGER"
      }
    ],
    "mode": "NULLABLE",
    "name": "split",
    "type": "RECORD"
  },
  {
    "fields": [
      {
        "mode": "NULLABLE",
        "name": "id",
        "type": "STRING"
      }
    ],
    "mode": "REPEATED",
    "name": "errorGroups",
    "type": "RECORD"
  },
  {
    "fields": [
      {
        "fields": [
          {
            "mode": "NULLABLE",
            "name": "container",
            "type": "STRING"
          },
          {
            "mode": "NULLABLE",
            "name": "location",
            "type": "STRING"
          },
          {
            "mode": "NULLABLE",
            "name": "id",
            "type": "STRING"
          }
        ],
        "mode": "NULLABLE",
        "name": "application",
        "type": "RECORD"
      },
      {
        "fields": [
          {
            "mode": "NULLABLE",
            "name": "id",
            "type": "STRING"
          },
          {
            "mode": "NULLABLE",
            "name": "environmentType",
            "type": "STRING"
          },
          {
            "mode": "NULLABLE",
            "name": "criticalityType",
            "type": "STRING"
          }
        ],
        "mode": "NULLABLE",
        "name": "service",
        "type": "RECORD"
      },
      {
        "fields": [
          {
            "mode": "NULLABLE",
            "name": "id",
            "type": "STRING"
          },
          {
            "mode": "NULLABLE",
            "name": "environmentType",
            "type": "STRING"
          },
          {
            "mode": "NULLABLE",
            "name": "criticalityType",
            "type": "STRING"
          }
        ],
        "mode": "NULLABLE",
        "name": "workload",
        "type": "RECORD"
      }
    ],
    "mode": "NULLABLE",
    "name": "apphub",
    "type": "RECORD"
  }
]
"""