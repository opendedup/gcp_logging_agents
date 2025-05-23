ACTIVITY_AUDIT_SCHEMA = """
[
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
            "name": "cluster_name",
            "type": "STRING"
          },
          {
            "mode": "NULLABLE",
            "name": "location",
            "type": "STRING"
          },
          {
            "mode": "NULLABLE",
            "name": "service",
            "type": "STRING"
          },
          {
            "mode": "NULLABLE",
            "name": "method",
            "type": "STRING"
          },
          {
            "mode": "NULLABLE",
            "name": "dataset_id",
            "type": "STRING"
          },
          {
            "mode": "NULLABLE",
            "name": "name",
            "type": "STRING"
          },
          {
            "mode": "NULLABLE",
            "name": "destination",
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
        "fields": [
          {
            "fields": [
              {
                "fields": [
                  {
                    "fields": [
                      {
                        "mode": "NULLABLE",
                        "name": "projectId",
                        "type": "STRING"
                      },
                      {
                        "mode": "NULLABLE",
                        "name": "datasetId",
                        "type": "STRING"
                      },
                      {
                        "mode": "NULLABLE",
                        "name": "tableId",
                        "type": "STRING"
                      }
                    ],
                    "mode": "NULLABLE",
                    "name": "tableName",
                    "type": "RECORD"
                  },
                  {
                    "fields": [
                      {
                        "mode": "NULLABLE",
                        "name": "friendlyName",
                        "type": "STRING"
                      },
                      {
                        "mode": "NULLABLE",
                        "name": "description",
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
                      }
                    ],
                    "mode": "NULLABLE",
                    "name": "info",
                    "type": "RECORD"
                  },
                  {
                    "mode": "NULLABLE",
                    "name": "schemaJson",
                    "type": "STRING"
                  },
                  {
                    "fields": [
                      {
                        "mode": "NULLABLE",
                        "name": "query",
                        "type": "STRING"
                      }
                    ],
                    "mode": "NULLABLE",
                    "name": "view",
                    "type": "RECORD"
                  },
                  {
                    "mode": "NULLABLE",
                    "name": "expireTime",
                    "type": "TIMESTAMP"
                  },
                  {
                    "mode": "NULLABLE",
                    "name": "createTime",
                    "type": "TIMESTAMP"
                  },
                  {
                    "mode": "NULLABLE",
                    "name": "truncateTime",
                    "type": "TIMESTAMP"
                  },
                  {
                    "mode": "NULLABLE",
                    "name": "updateTime",
                    "type": "TIMESTAMP"
                  },
                  {
                    "fields": [
                      {
                        "mode": "NULLABLE",
                        "name": "kmsKeyName",
                        "type": "STRING"
                      }
                    ],
                    "mode": "NULLABLE",
                    "name": "encryption",
                    "type": "RECORD"
                  }
                ],
                "mode": "NULLABLE",
                "name": "resource",
                "type": "RECORD"
              }
            ],
            "mode": "NULLABLE",
            "name": "tableInsertRequest",
            "type": "RECORD"
          },
          {
            "fields": [
              {
                "fields": [
                  {
                    "fields": [
                      {
                        "mode": "NULLABLE",
                        "name": "projectId",
                        "type": "STRING"
                      },
                      {
                        "mode": "NULLABLE",
                        "name": "datasetId",
                        "type": "STRING"
                      },
                      {
                        "mode": "NULLABLE",
                        "name": "tableId",
                        "type": "STRING"
                      }
                    ],
                    "mode": "NULLABLE",
                    "name": "tableName",
                    "type": "RECORD"
                  },
                  {
                    "fields": [
                      {
                        "mode": "NULLABLE",
                        "name": "friendlyName",
                        "type": "STRING"
                      },
                      {
                        "mode": "NULLABLE",
                        "name": "description",
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
                      }
                    ],
                    "mode": "NULLABLE",
                    "name": "info",
                    "type": "RECORD"
                  },
                  {
                    "mode": "NULLABLE",
                    "name": "schemaJson",
                    "type": "STRING"
                  },
                  {
                    "fields": [
                      {
                        "mode": "NULLABLE",
                        "name": "query",
                        "type": "STRING"
                      }
                    ],
                    "mode": "NULLABLE",
                    "name": "view",
                    "type": "RECORD"
                  },
                  {
                    "mode": "NULLABLE",
                    "name": "expireTime",
                    "type": "TIMESTAMP"
                  },
                  {
                    "mode": "NULLABLE",
                    "name": "createTime",
                    "type": "TIMESTAMP"
                  },
                  {
                    "mode": "NULLABLE",
                    "name": "truncateTime",
                    "type": "TIMESTAMP"
                  },
                  {
                    "mode": "NULLABLE",
                    "name": "updateTime",
                    "type": "TIMESTAMP"
                  },
                  {
                    "fields": [
                      {
                        "mode": "NULLABLE",
                        "name": "kmsKeyName",
                        "type": "STRING"
                      }
                    ],
                    "mode": "NULLABLE",
                    "name": "encryption",
                    "type": "RECORD"
                  }
                ],
                "mode": "NULLABLE",
                "name": "resource",
                "type": "RECORD"
              }
            ],
            "mode": "NULLABLE",
            "name": "tableUpdateRequest",
            "type": "RECORD"
          },
          {
            "fields": [
              {
                "mode": "NULLABLE",
                "name": "listAll",
                "type": "BOOLEAN"
              }
            ],
            "mode": "NULLABLE",
            "name": "datasetListRequest",
            "type": "RECORD"
          },
          {
            "fields": [
              {
                "fields": [
                  {
                    "fields": [
                      {
                        "mode": "NULLABLE",
                        "name": "projectId",
                        "type": "STRING"
                      },
                      {
                        "mode": "NULLABLE",
                        "name": "datasetId",
                        "type": "STRING"
                      }
                    ],
                    "mode": "NULLABLE",
                    "name": "datasetName",
                    "type": "RECORD"
                  },
                  {
                    "fields": [
                      {
                        "mode": "NULLABLE",
                        "name": "friendlyName",
                        "type": "STRING"
                      },
                      {
                        "mode": "NULLABLE",
                        "name": "description",
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
                      }
                    ],
                    "mode": "NULLABLE",
                    "name": "info",
                    "type": "RECORD"
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
                    "fields": [
                      {
                        "fields": [
                          {
                            "mode": "NULLABLE",
                            "name": "role",
                            "type": "STRING"
                          },
                          {
                            "mode": "NULLABLE",
                            "name": "groupEmail",
                            "type": "STRING"
                          },
                          {
                            "mode": "NULLABLE",
                            "name": "userEmail",
                            "type": "STRING"
                          },
                          {
                            "mode": "NULLABLE",
                            "name": "domain",
                            "type": "STRING"
                          },
                          {
                            "mode": "NULLABLE",
                            "name": "specialGroup",
                            "type": "STRING"
                          },
                          {
                            "fields": [
                              {
                                "mode": "NULLABLE",
                                "name": "projectId",
                                "type": "STRING"
                              },
                              {
                                "mode": "NULLABLE",
                                "name": "datasetId",
                                "type": "STRING"
                              },
                              {
                                "mode": "NULLABLE",
                                "name": "tableId",
                                "type": "STRING"
                              }
                            ],
                            "mode": "NULLABLE",
                            "name": "viewName",
                            "type": "RECORD"
                          }
                        ],
                        "mode": "REPEATED",
                        "name": "entries",
                        "type": "RECORD"
                      }
                    ],
                    "mode": "NULLABLE",
                    "name": "acl",
                    "type": "RECORD"
                  }
                ],
                "mode": "NULLABLE",
                "name": "resource",
                "type": "RECORD"
              }
            ],
            "mode": "NULLABLE",
            "name": "datasetInsertRequest",
            "type": "RECORD"
          },
          {
            "fields": [
              {
                "fields": [
                  {
                    "fields": [
                      {
                        "mode": "NULLABLE",
                        "name": "projectId",
                        "type": "STRING"
                      },
                      {
                        "mode": "NULLABLE",
                        "name": "datasetId",
                        "type": "STRING"
                      }
                    ],
                    "mode": "NULLABLE",
                    "name": "datasetName",
                    "type": "RECORD"
                  },
                  {
                    "fields": [
                      {
                        "mode": "NULLABLE",
                        "name": "friendlyName",
                        "type": "STRING"
                      },
                      {
                        "mode": "NULLABLE",
                        "name": "description",
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
                      }
                    ],
                    "mode": "NULLABLE",
                    "name": "info",
                    "type": "RECORD"
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
                    "fields": [
                      {
                        "fields": [
                          {
                            "mode": "NULLABLE",
                            "name": "role",
                            "type": "STRING"
                          },
                          {
                            "mode": "NULLABLE",
                            "name": "groupEmail",
                            "type": "STRING"
                          },
                          {
                            "mode": "NULLABLE",
                            "name": "userEmail",
                            "type": "STRING"
                          },
                          {
                            "mode": "NULLABLE",
                            "name": "domain",
                            "type": "STRING"
                          },
                          {
                            "mode": "NULLABLE",
                            "name": "specialGroup",
                            "type": "STRING"
                          },
                          {
                            "fields": [
                              {
                                "mode": "NULLABLE",
                                "name": "projectId",
                                "type": "STRING"
                              },
                              {
                                "mode": "NULLABLE",
                                "name": "datasetId",
                                "type": "STRING"
                              },
                              {
                                "mode": "NULLABLE",
                                "name": "tableId",
                                "type": "STRING"
                              }
                            ],
                            "mode": "NULLABLE",
                            "name": "viewName",
                            "type": "RECORD"
                          }
                        ],
                        "mode": "REPEATED",
                        "name": "entries",
                        "type": "RECORD"
                      }
                    ],
                    "mode": "NULLABLE",
                    "name": "acl",
                    "type": "RECORD"
                  }
                ],
                "mode": "NULLABLE",
                "name": "resource",
                "type": "RECORD"
              }
            ],
            "mode": "NULLABLE",
            "name": "datasetUpdateRequest",
            "type": "RECORD"
          },
          {
            "fields": [
              {
                "fields": [
                  {
                    "fields": [
                      {
                        "mode": "NULLABLE",
                        "name": "projectId",
                        "type": "STRING"
                      },
                      {
                        "mode": "NULLABLE",
                        "name": "jobId",
                        "type": "STRING"
                      },
                      {
                        "mode": "NULLABLE",
                        "name": "location",
                        "type": "STRING"
                      }
                    ],
                    "mode": "NULLABLE",
                    "name": "jobName",
                    "type": "RECORD"
                  },
                  {
                    "fields": [
                      {
                        "fields": [
                          {
                            "mode": "NULLABLE",
                            "name": "query",
                            "type": "STRING"
                          },
                          {
                            "fields": [
                              {
                                "mode": "NULLABLE",
                                "name": "projectId",
                                "type": "STRING"
                              },
                              {
                                "mode": "NULLABLE",
                                "name": "datasetId",
                                "type": "STRING"
                              },
                              {
                                "mode": "NULLABLE",
                                "name": "tableId",
                                "type": "STRING"
                              }
                            ],
                            "mode": "NULLABLE",
                            "name": "destinationTable",
                            "type": "RECORD"
                          },
                          {
                            "mode": "NULLABLE",
                            "name": "createDisposition",
                            "type": "STRING"
                          },
                          {
                            "mode": "NULLABLE",
                            "name": "writeDisposition",
                            "type": "STRING"
                          },
                          {
                            "fields": [
                              {
                                "mode": "NULLABLE",
                                "name": "projectId",
                                "type": "STRING"
                              },
                              {
                                "mode": "NULLABLE",
                                "name": "datasetId",
                                "type": "STRING"
                              }
                            ],
                            "mode": "NULLABLE",
                            "name": "defaultDataset",
                            "type": "RECORD"
                          },
                          {
                            "fields": [
                              {
                                "mode": "NULLABLE",
                                "name": "name",
                                "type": "STRING"
                              },
                              {
                                "mode": "REPEATED",
                                "name": "sourceUris",
                                "type": "STRING"
                              }
                            ],
                            "mode": "REPEATED",
                            "name": "tableDefinitions",
                            "type": "RECORD"
                          },
                          {
                            "mode": "NULLABLE",
                            "name": "queryPriority",
                            "type": "STRING"
                          },
                          {
                            "fields": [
                              {
                                "mode": "NULLABLE",
                                "name": "kmsKeyName",
                                "type": "STRING"
                              }
                            ],
                            "mode": "NULLABLE",
                            "name": "destinationTableEncryption",
                            "type": "RECORD"
                          },
                          {
                            "mode": "NULLABLE",
                            "name": "statementType",
                            "type": "STRING"
                          }
                        ],
                        "mode": "NULLABLE",
                        "name": "query",
                        "type": "RECORD"
                      },
                      {
                        "fields": [
                          {
                            "mode": "REPEATED",
                            "name": "sourceUris",
                            "type": "STRING"
                          },
                          {
                            "mode": "NULLABLE",
                            "name": "schemaJson",
                            "type": "STRING"
                          },
                          {
                            "fields": [
                              {
                                "mode": "NULLABLE",
                                "name": "projectId",
                                "type": "STRING"
                              },
                              {
                                "mode": "NULLABLE",
                                "name": "datasetId",
                                "type": "STRING"
                              },
                              {
                                "mode": "NULLABLE",
                                "name": "tableId",
                                "type": "STRING"
                              }
                            ],
                            "mode": "NULLABLE",
                            "name": "destinationTable",
                            "type": "RECORD"
                          },
                          {
                            "mode": "NULLABLE",
                            "name": "createDisposition",
                            "type": "STRING"
                          },
                          {
                            "mode": "NULLABLE",
                            "name": "writeDisposition",
                            "type": "STRING"
                          },
                          {
                            "fields": [
                              {
                                "mode": "NULLABLE",
                                "name": "kmsKeyName",
                                "type": "STRING"
                              }
                            ],
                            "mode": "NULLABLE",
                            "name": "destinationTableEncryption",
                            "type": "RECORD"
                          }
                        ],
                        "mode": "NULLABLE",
                        "name": "load",
                        "type": "RECORD"
                      },
                      {
                        "fields": [
                          {
                            "mode": "REPEATED",
                            "name": "destinationUris",
                            "type": "STRING"
                          },
                          {
                            "fields": [
                              {
                                "mode": "NULLABLE",
                                "name": "projectId",
                                "type": "STRING"
                              },
                              {
                                "mode": "NULLABLE",
                                "name": "datasetId",
                                "type": "STRING"
                              },
                              {
                                "mode": "NULLABLE",
                                "name": "tableId",
                                "type": "STRING"
                              }
                            ],
                            "mode": "NULLABLE",
                            "name": "sourceTable",
                            "type": "RECORD"
                          }
                        ],
                        "mode": "NULLABLE",
                        "name": "extract",
                        "type": "RECORD"
                      },
                      {
                        "fields": [
                          {
                            "fields": [
                              {
                                "mode": "NULLABLE",
                                "name": "projectId",
                                "type": "STRING"
                              },
                              {
                                "mode": "NULLABLE",
                                "name": "datasetId",
                                "type": "STRING"
                              },
                              {
                                "mode": "NULLABLE",
                                "name": "tableId",
                                "type": "STRING"
                              }
                            ],
                            "mode": "REPEATED",
                            "name": "sourceTables",
                            "type": "RECORD"
                          },
                          {
                            "fields": [
                              {
                                "mode": "NULLABLE",
                                "name": "projectId",
                                "type": "STRING"
                              },
                              {
                                "mode": "NULLABLE",
                                "name": "datasetId",
                                "type": "STRING"
                              },
                              {
                                "mode": "NULLABLE",
                                "name": "tableId",
                                "type": "STRING"
                              }
                            ],
                            "mode": "NULLABLE",
                            "name": "destinationTable",
                            "type": "RECORD"
                          },
                          {
                            "mode": "NULLABLE",
                            "name": "createDisposition",
                            "type": "STRING"
                          },
                          {
                            "mode": "NULLABLE",
                            "name": "writeDisposition",
                            "type": "STRING"
                          },
                          {
                            "fields": [
                              {
                                "mode": "NULLABLE",
                                "name": "kmsKeyName",
                                "type": "STRING"
                              }
                            ],
                            "mode": "NULLABLE",
                            "name": "destinationTableEncryption",
                            "type": "RECORD"
                          }
                        ],
                        "mode": "NULLABLE",
                        "name": "tableCopy",
                        "type": "RECORD"
                      },
                      {
                        "mode": "NULLABLE",
                        "name": "dryRun",
                        "type": "BOOLEAN"
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
                      }
                    ],
                    "mode": "NULLABLE",
                    "name": "jobConfiguration",
                    "type": "RECORD"
                  },
                  {
                    "fields": [
                      {
                        "mode": "NULLABLE",
                        "name": "state",
                        "type": "STRING"
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
                        "name": "error",
                        "type": "RECORD"
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
                        "mode": "REPEATED",
                        "name": "additionalErrors",
                        "type": "RECORD"
                      }
                    ],
                    "mode": "NULLABLE",
                    "name": "jobStatus",
                    "type": "RECORD"
                  },
                  {
                    "fields": [
                      {
                        "mode": "NULLABLE",
                        "name": "createTime",
                        "type": "TIMESTAMP"
                      },
                      {
                        "mode": "NULLABLE",
                        "name": "startTime",
                        "type": "TIMESTAMP"
                      },
                      {
                        "mode": "NULLABLE",
                        "name": "endTime",
                        "type": "TIMESTAMP"
                      },
                      {
                        "mode": "NULLABLE",
                        "name": "totalProcessedBytes",
                        "type": "INTEGER"
                      },
                      {
                        "mode": "NULLABLE",
                        "name": "totalBilledBytes",
                        "type": "INTEGER"
                      },
                      {
                        "mode": "NULLABLE",
                        "name": "billingTier",
                        "type": "INTEGER"
                      },
                      {
                        "mode": "NULLABLE",
                        "name": "totalSlotMs",
                        "type": "INTEGER"
                      },
                      {
                        "fields": [
                          {
                            "mode": "NULLABLE",
                            "name": "name",
                            "type": "STRING"
                          },
                          {
                            "mode": "NULLABLE",
                            "name": "slotMs",
                            "type": "INTEGER"
                          }
                        ],
                        "mode": "REPEATED",
                        "name": "reservationUsage",
                        "type": "RECORD"
                      },
                      {
                        "mode": "NULLABLE",
                        "name": "reservation",
                        "type": "STRING"
                      },
                      {
                        "fields": [
                          {
                            "mode": "NULLABLE",
                            "name": "projectId",
                            "type": "STRING"
                          },
                          {
                            "mode": "NULLABLE",
                            "name": "datasetId",
                            "type": "STRING"
                          },
                          {
                            "mode": "NULLABLE",
                            "name": "tableId",
                            "type": "STRING"
                          }
                        ],
                        "mode": "REPEATED",
                        "name": "referencedTables",
                        "type": "RECORD"
                      },
                      {
                        "mode": "NULLABLE",
                        "name": "totalTablesProcessed",
                        "type": "INTEGER"
                      },
                      {
                        "fields": [
                          {
                            "mode": "NULLABLE",
                            "name": "projectId",
                            "type": "STRING"
                          },
                          {
                            "mode": "NULLABLE",
                            "name": "datasetId",
                            "type": "STRING"
                          },
                          {
                            "mode": "NULLABLE",
                            "name": "tableId",
                            "type": "STRING"
                          }
                        ],
                        "mode": "REPEATED",
                        "name": "referencedViews",
                        "type": "RECORD"
                      },
                      {
                        "mode": "NULLABLE",
                        "name": "totalViewsProcessed",
                        "type": "INTEGER"
                      },
                      {
                        "mode": "NULLABLE",
                        "name": "queryOutputRowCount",
                        "type": "INTEGER"
                      },
                      {
                        "mode": "NULLABLE",
                        "name": "totalLoadOutputBytes",
                        "type": "INTEGER"
                      }
                    ],
                    "mode": "NULLABLE",
                    "name": "jobStatistics",
                    "type": "RECORD"
                  }
                ],
                "mode": "NULLABLE",
                "name": "resource",
                "type": "RECORD"
              }
            ],
            "mode": "NULLABLE",
            "name": "jobInsertRequest",
            "type": "RECORD"
          },
          {
            "fields": [
              {
                "mode": "NULLABLE",
                "name": "query",
                "type": "STRING"
              },
              {
                "mode": "NULLABLE",
                "name": "maxResults",
                "type": "INTEGER"
              },
              {
                "fields": [
                  {
                    "mode": "NULLABLE",
                    "name": "projectId",
                    "type": "STRING"
                  },
                  {
                    "mode": "NULLABLE",
                    "name": "datasetId",
                    "type": "STRING"
                  }
                ],
                "mode": "NULLABLE",
                "name": "defaultDataset",
                "type": "RECORD"
              },
              {
                "mode": "NULLABLE",
                "name": "projectId",
                "type": "STRING"
              },
              {
                "mode": "NULLABLE",
                "name": "dryRun",
                "type": "BOOLEAN"
              }
            ],
            "mode": "NULLABLE",
            "name": "jobQueryRequest",
            "type": "RECORD"
          },
          {
            "fields": [
              {
                "mode": "NULLABLE",
                "name": "maxResults",
                "type": "INTEGER"
              },
              {
                "mode": "NULLABLE",
                "name": "startRow",
                "type": "INTEGER"
              }
            ],
            "mode": "NULLABLE",
            "name": "jobGetQueryResultsRequest",
            "type": "RECORD"
          },
          {
            "fields": [
              {
                "mode": "NULLABLE",
                "name": "startRow",
                "type": "INTEGER"
              },
              {
                "mode": "NULLABLE",
                "name": "maxResults",
                "type": "INTEGER"
              }
            ],
            "mode": "NULLABLE",
            "name": "tableDataListRequest",
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
                "fields": [
                  {
                    "mode": "NULLABLE",
                    "name": "version",
                    "type": "INTEGER"
                  },
                  {
                    "fields": [
                      {
                        "mode": "NULLABLE",
                        "name": "role",
                        "type": "STRING"
                      },
                      {
                        "mode": "REPEATED",
                        "name": "members",
                        "type": "STRING"
                      },
                      {
                        "fields": [
                          {
                            "mode": "NULLABLE",
                            "name": "expression",
                            "type": "STRING"
                          },
                          {
                            "mode": "NULLABLE",
                            "name": "title",
                            "type": "STRING"
                          },
                          {
                            "mode": "NULLABLE",
                            "name": "description",
                            "type": "STRING"
                          },
                          {
                            "mode": "NULLABLE",
                            "name": "location",
                            "type": "STRING"
                          }
                        ],
                        "mode": "NULLABLE",
                        "name": "condition",
                        "type": "RECORD"
                      }
                    ],
                    "mode": "REPEATED",
                    "name": "bindings",
                    "type": "RECORD"
                  },
                  {
                    "fields": [
                      {
                        "mode": "NULLABLE",
                        "name": "service",
                        "type": "STRING"
                      },
                      {
                        "fields": [
                          {
                            "mode": "NULLABLE",
                            "name": "logType",
                            "type": "STRING"
                          },
                          {
                            "mode": "REPEATED",
                            "name": "exemptedMembers",
                            "type": "STRING"
                          }
                        ],
                        "mode": "REPEATED",
                        "name": "auditLogConfigs",
                        "type": "RECORD"
                      }
                    ],
                    "mode": "REPEATED",
                    "name": "auditConfigs",
                    "type": "RECORD"
                  },
                  {
                    "mode": "NULLABLE",
                    "name": "etag",
                    "type": "STRING"
                  }
                ],
                "mode": "NULLABLE",
                "name": "policy",
                "type": "RECORD"
              },
              {
                "fields": [
                  {
                    "mode": "REPEATED",
                    "name": "paths",
                    "type": "STRING"
                  }
                ],
                "mode": "NULLABLE",
                "name": "updateMask",
                "type": "RECORD"
              }
            ],
            "mode": "NULLABLE",
            "name": "setIamPolicyRequest",
            "type": "RECORD"
          },
          {
            "fields": [
              {
                "fields": [
                  {
                    "fields": [
                      {
                        "mode": "NULLABLE",
                        "name": "projectId",
                        "type": "STRING"
                      },
                      {
                        "mode": "NULLABLE",
                        "name": "datasetId",
                        "type": "STRING"
                      },
                      {
                        "mode": "NULLABLE",
                        "name": "tableId",
                        "type": "STRING"
                      }
                    ],
                    "mode": "NULLABLE",
                    "name": "tableName",
                    "type": "RECORD"
                  },
                  {
                    "fields": [
                      {
                        "mode": "NULLABLE",
                        "name": "friendlyName",
                        "type": "STRING"
                      },
                      {
                        "mode": "NULLABLE",
                        "name": "description",
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
                      }
                    ],
                    "mode": "NULLABLE",
                    "name": "info",
                    "type": "RECORD"
                  },
                  {
                    "mode": "NULLABLE",
                    "name": "schemaJson",
                    "type": "STRING"
                  },
                  {
                    "fields": [
                      {
                        "mode": "NULLABLE",
                        "name": "query",
                        "type": "STRING"
                      }
                    ],
                    "mode": "NULLABLE",
                    "name": "view",
                    "type": "RECORD"
                  },
                  {
                    "mode": "NULLABLE",
                    "name": "expireTime",
                    "type": "TIMESTAMP"
                  },
                  {
                    "mode": "NULLABLE",
                    "name": "createTime",
                    "type": "TIMESTAMP"
                  },
                  {
                    "mode": "NULLABLE",
                    "name": "truncateTime",
                    "type": "TIMESTAMP"
                  },
                  {
                    "mode": "NULLABLE",
                    "name": "updateTime",
                    "type": "TIMESTAMP"
                  },
                  {
                    "fields": [
                      {
                        "mode": "NULLABLE",
                        "name": "kmsKeyName",
                        "type": "STRING"
                      }
                    ],
                    "mode": "NULLABLE",
                    "name": "encryption",
                    "type": "RECORD"
                  }
                ],
                "mode": "NULLABLE",
                "name": "resource",
                "type": "RECORD"
              }
            ],
            "mode": "NULLABLE",
            "name": "tableInsertResponse",
            "type": "RECORD"
          },
          {
            "fields": [
              {
                "fields": [
                  {
                    "fields": [
                      {
                        "mode": "NULLABLE",
                        "name": "projectId",
                        "type": "STRING"
                      },
                      {
                        "mode": "NULLABLE",
                        "name": "datasetId",
                        "type": "STRING"
                      },
                      {
                        "mode": "NULLABLE",
                        "name": "tableId",
                        "type": "STRING"
                      }
                    ],
                    "mode": "NULLABLE",
                    "name": "tableName",
                    "type": "RECORD"
                  },
                  {
                    "fields": [
                      {
                        "mode": "NULLABLE",
                        "name": "friendlyName",
                        "type": "STRING"
                      },
                      {
                        "mode": "NULLABLE",
                        "name": "description",
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
                      }
                    ],
                    "mode": "NULLABLE",
                    "name": "info",
                    "type": "RECORD"
                  },
                  {
                    "mode": "NULLABLE",
                    "name": "schemaJson",
                    "type": "STRING"
                  },
                  {
                    "fields": [
                      {
                        "mode": "NULLABLE",
                        "name": "query",
                        "type": "STRING"
                      }
                    ],
                    "mode": "NULLABLE",
                    "name": "view",
                    "type": "RECORD"
                  },
                  {
                    "mode": "NULLABLE",
                    "name": "expireTime",
                    "type": "TIMESTAMP"
                  },
                  {
                    "mode": "NULLABLE",
                    "name": "createTime",
                    "type": "TIMESTAMP"
                  },
                  {
                    "mode": "NULLABLE",
                    "name": "truncateTime",
                    "type": "TIMESTAMP"
                  },
                  {
                    "mode": "NULLABLE",
                    "name": "updateTime",
                    "type": "TIMESTAMP"
                  },
                  {
                    "fields": [
                      {
                        "mode": "NULLABLE",
                        "name": "kmsKeyName",
                        "type": "STRING"
                      }
                    ],
                    "mode": "NULLABLE",
                    "name": "encryption",
                    "type": "RECORD"
                  }
                ],
                "mode": "NULLABLE",
                "name": "resource",
                "type": "RECORD"
              }
            ],
            "mode": "NULLABLE",
            "name": "tableUpdateResponse",
            "type": "RECORD"
          },
          {
            "fields": [
              {
                "fields": [
                  {
                    "fields": [
                      {
                        "mode": "NULLABLE",
                        "name": "projectId",
                        "type": "STRING"
                      },
                      {
                        "mode": "NULLABLE",
                        "name": "datasetId",
                        "type": "STRING"
                      }
                    ],
                    "mode": "NULLABLE",
                    "name": "datasetName",
                    "type": "RECORD"
                  },
                  {
                    "fields": [
                      {
                        "mode": "NULLABLE",
                        "name": "friendlyName",
                        "type": "STRING"
                      },
                      {
                        "mode": "NULLABLE",
                        "name": "description",
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
                      }
                    ],
                    "mode": "NULLABLE",
                    "name": "info",
                    "type": "RECORD"
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
                    "fields": [
                      {
                        "fields": [
                          {
                            "mode": "NULLABLE",
                            "name": "role",
                            "type": "STRING"
                          },
                          {
                            "mode": "NULLABLE",
                            "name": "groupEmail",
                            "type": "STRING"
                          },
                          {
                            "mode": "NULLABLE",
                            "name": "userEmail",
                            "type": "STRING"
                          },
                          {
                            "mode": "NULLABLE",
                            "name": "domain",
                            "type": "STRING"
                          },
                          {
                            "mode": "NULLABLE",
                            "name": "specialGroup",
                            "type": "STRING"
                          },
                          {
                            "fields": [
                              {
                                "mode": "NULLABLE",
                                "name": "projectId",
                                "type": "STRING"
                              },
                              {
                                "mode": "NULLABLE",
                                "name": "datasetId",
                                "type": "STRING"
                              },
                              {
                                "mode": "NULLABLE",
                                "name": "tableId",
                                "type": "STRING"
                              }
                            ],
                            "mode": "NULLABLE",
                            "name": "viewName",
                            "type": "RECORD"
                          }
                        ],
                        "mode": "REPEATED",
                        "name": "entries",
                        "type": "RECORD"
                      }
                    ],
                    "mode": "NULLABLE",
                    "name": "acl",
                    "type": "RECORD"
                  }
                ],
                "mode": "NULLABLE",
                "name": "resource",
                "type": "RECORD"
              }
            ],
            "mode": "NULLABLE",
            "name": "datasetInsertResponse",
            "type": "RECORD"
          },
          {
            "fields": [
              {
                "fields": [
                  {
                    "fields": [
                      {
                        "mode": "NULLABLE",
                        "name": "projectId",
                        "type": "STRING"
                      },
                      {
                        "mode": "NULLABLE",
                        "name": "datasetId",
                        "type": "STRING"
                      }
                    ],
                    "mode": "NULLABLE",
                    "name": "datasetName",
                    "type": "RECORD"
                  },
                  {
                    "fields": [
                      {
                        "mode": "NULLABLE",
                        "name": "friendlyName",
                        "type": "STRING"
                      },
                      {
                        "mode": "NULLABLE",
                        "name": "description",
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
                      }
                    ],
                    "mode": "NULLABLE",
                    "name": "info",
                    "type": "RECORD"
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
                    "fields": [
                      {
                        "fields": [
                          {
                            "mode": "NULLABLE",
                            "name": "role",
                            "type": "STRING"
                          },
                          {
                            "mode": "NULLABLE",
                            "name": "groupEmail",
                            "type": "STRING"
                          },
                          {
                            "mode": "NULLABLE",
                            "name": "userEmail",
                            "type": "STRING"
                          },
                          {
                            "mode": "NULLABLE",
                            "name": "domain",
                            "type": "STRING"
                          },
                          {
                            "mode": "NULLABLE",
                            "name": "specialGroup",
                            "type": "STRING"
                          },
                          {
                            "fields": [
                              {
                                "mode": "NULLABLE",
                                "name": "projectId",
                                "type": "STRING"
                              },
                              {
                                "mode": "NULLABLE",
                                "name": "datasetId",
                                "type": "STRING"
                              },
                              {
                                "mode": "NULLABLE",
                                "name": "tableId",
                                "type": "STRING"
                              }
                            ],
                            "mode": "NULLABLE",
                            "name": "viewName",
                            "type": "RECORD"
                          }
                        ],
                        "mode": "REPEATED",
                        "name": "entries",
                        "type": "RECORD"
                      }
                    ],
                    "mode": "NULLABLE",
                    "name": "acl",
                    "type": "RECORD"
                  }
                ],
                "mode": "NULLABLE",
                "name": "resource",
                "type": "RECORD"
              }
            ],
            "mode": "NULLABLE",
            "name": "datasetUpdateResponse",
            "type": "RECORD"
          },
          {
            "fields": [
              {
                "fields": [
                  {
                    "fields": [
                      {
                        "mode": "NULLABLE",
                        "name": "projectId",
                        "type": "STRING"
                      },
                      {
                        "mode": "NULLABLE",
                        "name": "jobId",
                        "type": "STRING"
                      },
                      {
                        "mode": "NULLABLE",
                        "name": "location",
                        "type": "STRING"
                      }
                    ],
                    "mode": "NULLABLE",
                    "name": "jobName",
                    "type": "RECORD"
                  },
                  {
                    "fields": [
                      {
                        "fields": [
                          {
                            "mode": "NULLABLE",
                            "name": "query",
                            "type": "STRING"
                          },
                          {
                            "fields": [
                              {
                                "mode": "NULLABLE",
                                "name": "projectId",
                                "type": "STRING"
                              },
                              {
                                "mode": "NULLABLE",
                                "name": "datasetId",
                                "type": "STRING"
                              },
                              {
                                "mode": "NULLABLE",
                                "name": "tableId",
                                "type": "STRING"
                              }
                            ],
                            "mode": "NULLABLE",
                            "name": "destinationTable",
                            "type": "RECORD"
                          },
                          {
                            "mode": "NULLABLE",
                            "name": "createDisposition",
                            "type": "STRING"
                          },
                          {
                            "mode": "NULLABLE",
                            "name": "writeDisposition",
                            "type": "STRING"
                          },
                          {
                            "fields": [
                              {
                                "mode": "NULLABLE",
                                "name": "projectId",
                                "type": "STRING"
                              },
                              {
                                "mode": "NULLABLE",
                                "name": "datasetId",
                                "type": "STRING"
                              }
                            ],
                            "mode": "NULLABLE",
                            "name": "defaultDataset",
                            "type": "RECORD"
                          },
                          {
                            "fields": [
                              {
                                "mode": "NULLABLE",
                                "name": "name",
                                "type": "STRING"
                              },
                              {
                                "mode": "REPEATED",
                                "name": "sourceUris",
                                "type": "STRING"
                              }
                            ],
                            "mode": "REPEATED",
                            "name": "tableDefinitions",
                            "type": "RECORD"
                          },
                          {
                            "mode": "NULLABLE",
                            "name": "queryPriority",
                            "type": "STRING"
                          },
                          {
                            "fields": [
                              {
                                "mode": "NULLABLE",
                                "name": "kmsKeyName",
                                "type": "STRING"
                              }
                            ],
                            "mode": "NULLABLE",
                            "name": "destinationTableEncryption",
                            "type": "RECORD"
                          },
                          {
                            "mode": "NULLABLE",
                            "name": "statementType",
                            "type": "STRING"
                          }
                        ],
                        "mode": "NULLABLE",
                        "name": "query",
                        "type": "RECORD"
                      },
                      {
                        "fields": [
                          {
                            "mode": "REPEATED",
                            "name": "sourceUris",
                            "type": "STRING"
                          },
                          {
                            "mode": "NULLABLE",
                            "name": "schemaJson",
                            "type": "STRING"
                          },
                          {
                            "fields": [
                              {
                                "mode": "NULLABLE",
                                "name": "projectId",
                                "type": "STRING"
                              },
                              {
                                "mode": "NULLABLE",
                                "name": "datasetId",
                                "type": "STRING"
                              },
                              {
                                "mode": "NULLABLE",
                                "name": "tableId",
                                "type": "STRING"
                              }
                            ],
                            "mode": "NULLABLE",
                            "name": "destinationTable",
                            "type": "RECORD"
                          },
                          {
                            "mode": "NULLABLE",
                            "name": "createDisposition",
                            "type": "STRING"
                          },
                          {
                            "mode": "NULLABLE",
                            "name": "writeDisposition",
                            "type": "STRING"
                          },
                          {
                            "fields": [
                              {
                                "mode": "NULLABLE",
                                "name": "kmsKeyName",
                                "type": "STRING"
                              }
                            ],
                            "mode": "NULLABLE",
                            "name": "destinationTableEncryption",
                            "type": "RECORD"
                          }
                        ],
                        "mode": "NULLABLE",
                        "name": "load",
                        "type": "RECORD"
                      },
                      {
                        "fields": [
                          {
                            "mode": "REPEATED",
                            "name": "destinationUris",
                            "type": "STRING"
                          },
                          {
                            "fields": [
                              {
                                "mode": "NULLABLE",
                                "name": "projectId",
                                "type": "STRING"
                              },
                              {
                                "mode": "NULLABLE",
                                "name": "datasetId",
                                "type": "STRING"
                              },
                              {
                                "mode": "NULLABLE",
                                "name": "tableId",
                                "type": "STRING"
                              }
                            ],
                            "mode": "NULLABLE",
                            "name": "sourceTable",
                            "type": "RECORD"
                          }
                        ],
                        "mode": "NULLABLE",
                        "name": "extract",
                        "type": "RECORD"
                      },
                      {
                        "fields": [
                          {
                            "fields": [
                              {
                                "mode": "NULLABLE",
                                "name": "projectId",
                                "type": "STRING"
                              },
                              {
                                "mode": "NULLABLE",
                                "name": "datasetId",
                                "type": "STRING"
                              },
                              {
                                "mode": "NULLABLE",
                                "name": "tableId",
                                "type": "STRING"
                              }
                            ],
                            "mode": "REPEATED",
                            "name": "sourceTables",
                            "type": "RECORD"
                          },
                          {
                            "fields": [
                              {
                                "mode": "NULLABLE",
                                "name": "projectId",
                                "type": "STRING"
                              },
                              {
                                "mode": "NULLABLE",
                                "name": "datasetId",
                                "type": "STRING"
                              },
                              {
                                "mode": "NULLABLE",
                                "name": "tableId",
                                "type": "STRING"
                              }
                            ],
                            "mode": "NULLABLE",
                            "name": "destinationTable",
                            "type": "RECORD"
                          },
                          {
                            "mode": "NULLABLE",
                            "name": "createDisposition",
                            "type": "STRING"
                          },
                          {
                            "mode": "NULLABLE",
                            "name": "writeDisposition",
                            "type": "STRING"
                          },
                          {
                            "fields": [
                              {
                                "mode": "NULLABLE",
                                "name": "kmsKeyName",
                                "type": "STRING"
                              }
                            ],
                            "mode": "NULLABLE",
                            "name": "destinationTableEncryption",
                            "type": "RECORD"
                          }
                        ],
                        "mode": "NULLABLE",
                        "name": "tableCopy",
                        "type": "RECORD"
                      },
                      {
                        "mode": "NULLABLE",
                        "name": "dryRun",
                        "type": "BOOLEAN"
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
                      }
                    ],
                    "mode": "NULLABLE",
                    "name": "jobConfiguration",
                    "type": "RECORD"
                  },
                  {
                    "fields": [
                      {
                        "mode": "NULLABLE",
                        "name": "state",
                        "type": "STRING"
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
                        "name": "error",
                        "type": "RECORD"
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
                        "mode": "REPEATED",
                        "name": "additionalErrors",
                        "type": "RECORD"
                      }
                    ],
                    "mode": "NULLABLE",
                    "name": "jobStatus",
                    "type": "RECORD"
                  },
                  {
                    "fields": [
                      {
                        "mode": "NULLABLE",
                        "name": "createTime",
                        "type": "TIMESTAMP"
                      },
                      {
                        "mode": "NULLABLE",
                        "name": "startTime",
                        "type": "TIMESTAMP"
                      },
                      {
                        "mode": "NULLABLE",
                        "name": "endTime",
                        "type": "TIMESTAMP"
                      },
                      {
                        "mode": "NULLABLE",
                        "name": "totalProcessedBytes",
                        "type": "INTEGER"
                      },
                      {
                        "mode": "NULLABLE",
                        "name": "totalBilledBytes",
                        "type": "INTEGER"
                      },
                      {
                        "mode": "NULLABLE",
                        "name": "billingTier",
                        "type": "INTEGER"
                      },
                      {
                        "mode": "NULLABLE",
                        "name": "totalSlotMs",
                        "type": "INTEGER"
                      },
                      {
                        "fields": [
                          {
                            "mode": "NULLABLE",
                            "name": "name",
                            "type": "STRING"
                          },
                          {
                            "mode": "NULLABLE",
                            "name": "slotMs",
                            "type": "INTEGER"
                          }
                        ],
                        "mode": "REPEATED",
                        "name": "reservationUsage",
                        "type": "RECORD"
                      },
                      {
                        "mode": "NULLABLE",
                        "name": "reservation",
                        "type": "STRING"
                      },
                      {
                        "fields": [
                          {
                            "mode": "NULLABLE",
                            "name": "projectId",
                            "type": "STRING"
                          },
                          {
                            "mode": "NULLABLE",
                            "name": "datasetId",
                            "type": "STRING"
                          },
                          {
                            "mode": "NULLABLE",
                            "name": "tableId",
                            "type": "STRING"
                          }
                        ],
                        "mode": "REPEATED",
                        "name": "referencedTables",
                        "type": "RECORD"
                      },
                      {
                        "mode": "NULLABLE",
                        "name": "totalTablesProcessed",
                        "type": "INTEGER"
                      },
                      {
                        "fields": [
                          {
                            "mode": "NULLABLE",
                            "name": "projectId",
                            "type": "STRING"
                          },
                          {
                            "mode": "NULLABLE",
                            "name": "datasetId",
                            "type": "STRING"
                          },
                          {
                            "mode": "NULLABLE",
                            "name": "tableId",
                            "type": "STRING"
                          }
                        ],
                        "mode": "REPEATED",
                        "name": "referencedViews",
                        "type": "RECORD"
                      },
                      {
                        "mode": "NULLABLE",
                        "name": "totalViewsProcessed",
                        "type": "INTEGER"
                      },
                      {
                        "mode": "NULLABLE",
                        "name": "queryOutputRowCount",
                        "type": "INTEGER"
                      },
                      {
                        "mode": "NULLABLE",
                        "name": "totalLoadOutputBytes",
                        "type": "INTEGER"
                      }
                    ],
                    "mode": "NULLABLE",
                    "name": "jobStatistics",
                    "type": "RECORD"
                  }
                ],
                "mode": "NULLABLE",
                "name": "resource",
                "type": "RECORD"
              }
            ],
            "mode": "NULLABLE",
            "name": "jobInsertResponse",
            "type": "RECORD"
          },
          {
            "fields": [
              {
                "mode": "NULLABLE",
                "name": "totalResults",
                "type": "INTEGER"
              },
              {
                "fields": [
                  {
                    "fields": [
                      {
                        "mode": "NULLABLE",
                        "name": "projectId",
                        "type": "STRING"
                      },
                      {
                        "mode": "NULLABLE",
                        "name": "jobId",
                        "type": "STRING"
                      },
                      {
                        "mode": "NULLABLE",
                        "name": "location",
                        "type": "STRING"
                      }
                    ],
                    "mode": "NULLABLE",
                    "name": "jobName",
                    "type": "RECORD"
                  },
                  {
                    "fields": [
                      {
                        "fields": [
                          {
                            "mode": "NULLABLE",
                            "name": "query",
                            "type": "STRING"
                          },
                          {
                            "fields": [
                              {
                                "mode": "NULLABLE",
                                "name": "projectId",
                                "type": "STRING"
                              },
                              {
                                "mode": "NULLABLE",
                                "name": "datasetId",
                                "type": "STRING"
                              },
                              {
                                "mode": "NULLABLE",
                                "name": "tableId",
                                "type": "STRING"
                              }
                            ],
                            "mode": "NULLABLE",
                            "name": "destinationTable",
                            "type": "RECORD"
                          },
                          {
                            "mode": "NULLABLE",
                            "name": "createDisposition",
                            "type": "STRING"
                          },
                          {
                            "mode": "NULLABLE",
                            "name": "writeDisposition",
                            "type": "STRING"
                          },
                          {
                            "fields": [
                              {
                                "mode": "NULLABLE",
                                "name": "projectId",
                                "type": "STRING"
                              },
                              {
                                "mode": "NULLABLE",
                                "name": "datasetId",
                                "type": "STRING"
                              }
                            ],
                            "mode": "NULLABLE",
                            "name": "defaultDataset",
                            "type": "RECORD"
                          },
                          {
                            "fields": [
                              {
                                "mode": "NULLABLE",
                                "name": "name",
                                "type": "STRING"
                              },
                              {
                                "mode": "REPEATED",
                                "name": "sourceUris",
                                "type": "STRING"
                              }
                            ],
                            "mode": "REPEATED",
                            "name": "tableDefinitions",
                            "type": "RECORD"
                          },
                          {
                            "mode": "NULLABLE",
                            "name": "queryPriority",
                            "type": "STRING"
                          },
                          {
                            "fields": [
                              {
                                "mode": "NULLABLE",
                                "name": "kmsKeyName",
                                "type": "STRING"
                              }
                            ],
                            "mode": "NULLABLE",
                            "name": "destinationTableEncryption",
                            "type": "RECORD"
                          },
                          {
                            "mode": "NULLABLE",
                            "name": "statementType",
                            "type": "STRING"
                          }
                        ],
                        "mode": "NULLABLE",
                        "name": "query",
                        "type": "RECORD"
                      },
                      {
                        "fields": [
                          {
                            "mode": "REPEATED",
                            "name": "sourceUris",
                            "type": "STRING"
                          },
                          {
                            "mode": "NULLABLE",
                            "name": "schemaJson",
                            "type": "STRING"
                          },
                          {
                            "fields": [
                              {
                                "mode": "NULLABLE",
                                "name": "projectId",
                                "type": "STRING"
                              },
                              {
                                "mode": "NULLABLE",
                                "name": "datasetId",
                                "type": "STRING"
                              },
                              {
                                "mode": "NULLABLE",
                                "name": "tableId",
                                "type": "STRING"
                              }
                            ],
                            "mode": "NULLABLE",
                            "name": "destinationTable",
                            "type": "RECORD"
                          },
                          {
                            "mode": "NULLABLE",
                            "name": "createDisposition",
                            "type": "STRING"
                          },
                          {
                            "mode": "NULLABLE",
                            "name": "writeDisposition",
                            "type": "STRING"
                          },
                          {
                            "fields": [
                              {
                                "mode": "NULLABLE",
                                "name": "kmsKeyName",
                                "type": "STRING"
                              }
                            ],
                            "mode": "NULLABLE",
                            "name": "destinationTableEncryption",
                            "type": "RECORD"
                          }
                        ],
                        "mode": "NULLABLE",
                        "name": "load",
                        "type": "RECORD"
                      },
                      {
                        "fields": [
                          {
                            "mode": "REPEATED",
                            "name": "destinationUris",
                            "type": "STRING"
                          },
                          {
                            "fields": [
                              {
                                "mode": "NULLABLE",
                                "name": "projectId",
                                "type": "STRING"
                              },
                              {
                                "mode": "NULLABLE",
                                "name": "datasetId",
                                "type": "STRING"
                              },
                              {
                                "mode": "NULLABLE",
                                "name": "tableId",
                                "type": "STRING"
                              }
                            ],
                            "mode": "NULLABLE",
                            "name": "sourceTable",
                            "type": "RECORD"
                          }
                        ],
                        "mode": "NULLABLE",
                        "name": "extract",
                        "type": "RECORD"
                      },
                      {
                        "fields": [
                          {
                            "fields": [
                              {
                                "mode": "NULLABLE",
                                "name": "projectId",
                                "type": "STRING"
                              },
                              {
                                "mode": "NULLABLE",
                                "name": "datasetId",
                                "type": "STRING"
                              },
                              {
                                "mode": "NULLABLE",
                                "name": "tableId",
                                "type": "STRING"
                              }
                            ],
                            "mode": "REPEATED",
                            "name": "sourceTables",
                            "type": "RECORD"
                          },
                          {
                            "fields": [
                              {
                                "mode": "NULLABLE",
                                "name": "projectId",
                                "type": "STRING"
                              },
                              {
                                "mode": "NULLABLE",
                                "name": "datasetId",
                                "type": "STRING"
                              },
                              {
                                "mode": "NULLABLE",
                                "name": "tableId",
                                "type": "STRING"
                              }
                            ],
                            "mode": "NULLABLE",
                            "name": "destinationTable",
                            "type": "RECORD"
                          },
                          {
                            "mode": "NULLABLE",
                            "name": "createDisposition",
                            "type": "STRING"
                          },
                          {
                            "mode": "NULLABLE",
                            "name": "writeDisposition",
                            "type": "STRING"
                          },
                          {
                            "fields": [
                              {
                                "mode": "NULLABLE",
                                "name": "kmsKeyName",
                                "type": "STRING"
                              }
                            ],
                            "mode": "NULLABLE",
                            "name": "destinationTableEncryption",
                            "type": "RECORD"
                          }
                        ],
                        "mode": "NULLABLE",
                        "name": "tableCopy",
                        "type": "RECORD"
                      },
                      {
                        "mode": "NULLABLE",
                        "name": "dryRun",
                        "type": "BOOLEAN"
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
                      }
                    ],
                    "mode": "NULLABLE",
                    "name": "jobConfiguration",
                    "type": "RECORD"
                  },
                  {
                    "fields": [
                      {
                        "mode": "NULLABLE",
                        "name": "state",
                        "type": "STRING"
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
                        "name": "error",
                        "type": "RECORD"
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
                        "mode": "REPEATED",
                        "name": "additionalErrors",
                        "type": "RECORD"
                      }
                    ],
                    "mode": "NULLABLE",
                    "name": "jobStatus",
                    "type": "RECORD"
                  },
                  {
                    "fields": [
                      {
                        "mode": "NULLABLE",
                        "name": "createTime",
                        "type": "TIMESTAMP"
                      },
                      {
                        "mode": "NULLABLE",
                        "name": "startTime",
                        "type": "TIMESTAMP"
                      },
                      {
                        "mode": "NULLABLE",
                        "name": "endTime",
                        "type": "TIMESTAMP"
                      },
                      {
                        "mode": "NULLABLE",
                        "name": "totalProcessedBytes",
                        "type": "INTEGER"
                      },
                      {
                        "mode": "NULLABLE",
                        "name": "totalBilledBytes",
                        "type": "INTEGER"
                      },
                      {
                        "mode": "NULLABLE",
                        "name": "billingTier",
                        "type": "INTEGER"
                      },
                      {
                        "mode": "NULLABLE",
                        "name": "totalSlotMs",
                        "type": "INTEGER"
                      },
                      {
                        "fields": [
                          {
                            "mode": "NULLABLE",
                            "name": "name",
                            "type": "STRING"
                          },
                          {
                            "mode": "NULLABLE",
                            "name": "slotMs",
                            "type": "INTEGER"
                          }
                        ],
                        "mode": "REPEATED",
                        "name": "reservationUsage",
                        "type": "RECORD"
                      },
                      {
                        "mode": "NULLABLE",
                        "name": "reservation",
                        "type": "STRING"
                      },
                      {
                        "fields": [
                          {
                            "mode": "NULLABLE",
                            "name": "projectId",
                            "type": "STRING"
                          },
                          {
                            "mode": "NULLABLE",
                            "name": "datasetId",
                            "type": "STRING"
                          },
                          {
                            "mode": "NULLABLE",
                            "name": "tableId",
                            "type": "STRING"
                          }
                        ],
                        "mode": "REPEATED",
                        "name": "referencedTables",
                        "type": "RECORD"
                      },
                      {
                        "mode": "NULLABLE",
                        "name": "totalTablesProcessed",
                        "type": "INTEGER"
                      },
                      {
                        "fields": [
                          {
                            "mode": "NULLABLE",
                            "name": "projectId",
                            "type": "STRING"
                          },
                          {
                            "mode": "NULLABLE",
                            "name": "datasetId",
                            "type": "STRING"
                          },
                          {
                            "mode": "NULLABLE",
                            "name": "tableId",
                            "type": "STRING"
                          }
                        ],
                        "mode": "REPEATED",
                        "name": "referencedViews",
                        "type": "RECORD"
                      },
                      {
                        "mode": "NULLABLE",
                        "name": "totalViewsProcessed",
                        "type": "INTEGER"
                      },
                      {
                        "mode": "NULLABLE",
                        "name": "queryOutputRowCount",
                        "type": "INTEGER"
                      },
                      {
                        "mode": "NULLABLE",
                        "name": "totalLoadOutputBytes",
                        "type": "INTEGER"
                      }
                    ],
                    "mode": "NULLABLE",
                    "name": "jobStatistics",
                    "type": "RECORD"
                  }
                ],
                "mode": "NULLABLE",
                "name": "job",
                "type": "RECORD"
              }
            ],
            "mode": "NULLABLE",
            "name": "jobQueryResponse",
            "type": "RECORD"
          },
          {
            "fields": [
              {
                "mode": "NULLABLE",
                "name": "totalResults",
                "type": "INTEGER"
              },
              {
                "fields": [
                  {
                    "fields": [
                      {
                        "mode": "NULLABLE",
                        "name": "projectId",
                        "type": "STRING"
                      },
                      {
                        "mode": "NULLABLE",
                        "name": "jobId",
                        "type": "STRING"
                      },
                      {
                        "mode": "NULLABLE",
                        "name": "location",
                        "type": "STRING"
                      }
                    ],
                    "mode": "NULLABLE",
                    "name": "jobName",
                    "type": "RECORD"
                  },
                  {
                    "fields": [
                      {
                        "fields": [
                          {
                            "mode": "NULLABLE",
                            "name": "query",
                            "type": "STRING"
                          },
                          {
                            "fields": [
                              {
                                "mode": "NULLABLE",
                                "name": "projectId",
                                "type": "STRING"
                              },
                              {
                                "mode": "NULLABLE",
                                "name": "datasetId",
                                "type": "STRING"
                              },
                              {
                                "mode": "NULLABLE",
                                "name": "tableId",
                                "type": "STRING"
                              }
                            ],
                            "mode": "NULLABLE",
                            "name": "destinationTable",
                            "type": "RECORD"
                          },
                          {
                            "mode": "NULLABLE",
                            "name": "createDisposition",
                            "type": "STRING"
                          },
                          {
                            "mode": "NULLABLE",
                            "name": "writeDisposition",
                            "type": "STRING"
                          },
                          {
                            "fields": [
                              {
                                "mode": "NULLABLE",
                                "name": "projectId",
                                "type": "STRING"
                              },
                              {
                                "mode": "NULLABLE",
                                "name": "datasetId",
                                "type": "STRING"
                              }
                            ],
                            "mode": "NULLABLE",
                            "name": "defaultDataset",
                            "type": "RECORD"
                          },
                          {
                            "fields": [
                              {
                                "mode": "NULLABLE",
                                "name": "name",
                                "type": "STRING"
                              },
                              {
                                "mode": "REPEATED",
                                "name": "sourceUris",
                                "type": "STRING"
                              }
                            ],
                            "mode": "REPEATED",
                            "name": "tableDefinitions",
                            "type": "RECORD"
                          },
                          {
                            "mode": "NULLABLE",
                            "name": "queryPriority",
                            "type": "STRING"
                          },
                          {
                            "fields": [
                              {
                                "mode": "NULLABLE",
                                "name": "kmsKeyName",
                                "type": "STRING"
                              }
                            ],
                            "mode": "NULLABLE",
                            "name": "destinationTableEncryption",
                            "type": "RECORD"
                          },
                          {
                            "mode": "NULLABLE",
                            "name": "statementType",
                            "type": "STRING"
                          }
                        ],
                        "mode": "NULLABLE",
                        "name": "query",
                        "type": "RECORD"
                      },
                      {
                        "fields": [
                          {
                            "mode": "REPEATED",
                            "name": "sourceUris",
                            "type": "STRING"
                          },
                          {
                            "mode": "NULLABLE",
                            "name": "schemaJson",
                            "type": "STRING"
                          },
                          {
                            "fields": [
                              {
                                "mode": "NULLABLE",
                                "name": "projectId",
                                "type": "STRING"
                              },
                              {
                                "mode": "NULLABLE",
                                "name": "datasetId",
                                "type": "STRING"
                              },
                              {
                                "mode": "NULLABLE",
                                "name": "tableId",
                                "type": "STRING"
                              }
                            ],
                            "mode": "NULLABLE",
                            "name": "destinationTable",
                            "type": "RECORD"
                          },
                          {
                            "mode": "NULLABLE",
                            "name": "createDisposition",
                            "type": "STRING"
                          },
                          {
                            "mode": "NULLABLE",
                            "name": "writeDisposition",
                            "type": "STRING"
                          },
                          {
                            "fields": [
                              {
                                "mode": "NULLABLE",
                                "name": "kmsKeyName",
                                "type": "STRING"
                              }
                            ],
                            "mode": "NULLABLE",
                            "name": "destinationTableEncryption",
                            "type": "RECORD"
                          }
                        ],
                        "mode": "NULLABLE",
                        "name": "load",
                        "type": "RECORD"
                      },
                      {
                        "fields": [
                          {
                            "mode": "REPEATED",
                            "name": "destinationUris",
                            "type": "STRING"
                          },
                          {
                            "fields": [
                              {
                                "mode": "NULLABLE",
                                "name": "projectId",
                                "type": "STRING"
                              },
                              {
                                "mode": "NULLABLE",
                                "name": "datasetId",
                                "type": "STRING"
                              },
                              {
                                "mode": "NULLABLE",
                                "name": "tableId",
                                "type": "STRING"
                              }
                            ],
                            "mode": "NULLABLE",
                            "name": "sourceTable",
                            "type": "RECORD"
                          }
                        ],
                        "mode": "NULLABLE",
                        "name": "extract",
                        "type": "RECORD"
                      },
                      {
                        "fields": [
                          {
                            "fields": [
                              {
                                "mode": "NULLABLE",
                                "name": "projectId",
                                "type": "STRING"
                              },
                              {
                                "mode": "NULLABLE",
                                "name": "datasetId",
                                "type": "STRING"
                              },
                              {
                                "mode": "NULLABLE",
                                "name": "tableId",
                                "type": "STRING"
                              }
                            ],
                            "mode": "REPEATED",
                            "name": "sourceTables",
                            "type": "RECORD"
                          },
                          {
                            "fields": [
                              {
                                "mode": "NULLABLE",
                                "name": "projectId",
                                "type": "STRING"
                              },
                              {
                                "mode": "NULLABLE",
                                "name": "datasetId",
                                "type": "STRING"
                              },
                              {
                                "mode": "NULLABLE",
                                "name": "tableId",
                                "type": "STRING"
                              }
                            ],
                            "mode": "NULLABLE",
                            "name": "destinationTable",
                            "type": "RECORD"
                          },
                          {
                            "mode": "NULLABLE",
                            "name": "createDisposition",
                            "type": "STRING"
                          },
                          {
                            "mode": "NULLABLE",
                            "name": "writeDisposition",
                            "type": "STRING"
                          },
                          {
                            "fields": [
                              {
                                "mode": "NULLABLE",
                                "name": "kmsKeyName",
                                "type": "STRING"
                              }
                            ],
                            "mode": "NULLABLE",
                            "name": "destinationTableEncryption",
                            "type": "RECORD"
                          }
                        ],
                        "mode": "NULLABLE",
                        "name": "tableCopy",
                        "type": "RECORD"
                      },
                      {
                        "mode": "NULLABLE",
                        "name": "dryRun",
                        "type": "BOOLEAN"
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
                      }
                    ],
                    "mode": "NULLABLE",
                    "name": "jobConfiguration",
                    "type": "RECORD"
                  },
                  {
                    "fields": [
                      {
                        "mode": "NULLABLE",
                        "name": "state",
                        "type": "STRING"
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
                        "name": "error",
                        "type": "RECORD"
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
                        "mode": "REPEATED",
                        "name": "additionalErrors",
                        "type": "RECORD"
                      }
                    ],
                    "mode": "NULLABLE",
                    "name": "jobStatus",
                    "type": "RECORD"
                  },
                  {
                    "fields": [
                      {
                        "mode": "NULLABLE",
                        "name": "createTime",
                        "type": "TIMESTAMP"
                      },
                      {
                        "mode": "NULLABLE",
                        "name": "startTime",
                        "type": "TIMESTAMP"
                      },
                      {
                        "mode": "NULLABLE",
                        "name": "endTime",
                        "type": "TIMESTAMP"
                      },
                      {
                        "mode": "NULLABLE",
                        "name": "totalProcessedBytes",
                        "type": "INTEGER"
                      },
                      {
                        "mode": "NULLABLE",
                        "name": "totalBilledBytes",
                        "type": "INTEGER"
                      },
                      {
                        "mode": "NULLABLE",
                        "name": "billingTier",
                        "type": "INTEGER"
                      },
                      {
                        "mode": "NULLABLE",
                        "name": "totalSlotMs",
                        "type": "INTEGER"
                      },
                      {
                        "fields": [
                          {
                            "mode": "NULLABLE",
                            "name": "name",
                            "type": "STRING"
                          },
                          {
                            "mode": "NULLABLE",
                            "name": "slotMs",
                            "type": "INTEGER"
                          }
                        ],
                        "mode": "REPEATED",
                        "name": "reservationUsage",
                        "type": "RECORD"
                      },
                      {
                        "mode": "NULLABLE",
                        "name": "reservation",
                        "type": "STRING"
                      },
                      {
                        "fields": [
                          {
                            "mode": "NULLABLE",
                            "name": "projectId",
                            "type": "STRING"
                          },
                          {
                            "mode": "NULLABLE",
                            "name": "datasetId",
                            "type": "STRING"
                          },
                          {
                            "mode": "NULLABLE",
                            "name": "tableId",
                            "type": "STRING"
                          }
                        ],
                        "mode": "REPEATED",
                        "name": "referencedTables",
                        "type": "RECORD"
                      },
                      {
                        "mode": "NULLABLE",
                        "name": "totalTablesProcessed",
                        "type": "INTEGER"
                      },
                      {
                        "fields": [
                          {
                            "mode": "NULLABLE",
                            "name": "projectId",
                            "type": "STRING"
                          },
                          {
                            "mode": "NULLABLE",
                            "name": "datasetId",
                            "type": "STRING"
                          },
                          {
                            "mode": "NULLABLE",
                            "name": "tableId",
                            "type": "STRING"
                          }
                        ],
                        "mode": "REPEATED",
                        "name": "referencedViews",
                        "type": "RECORD"
                      },
                      {
                        "mode": "NULLABLE",
                        "name": "totalViewsProcessed",
                        "type": "INTEGER"
                      },
                      {
                        "mode": "NULLABLE",
                        "name": "queryOutputRowCount",
                        "type": "INTEGER"
                      },
                      {
                        "mode": "NULLABLE",
                        "name": "totalLoadOutputBytes",
                        "type": "INTEGER"
                      }
                    ],
                    "mode": "NULLABLE",
                    "name": "jobStatistics",
                    "type": "RECORD"
                  }
                ],
                "mode": "NULLABLE",
                "name": "job",
                "type": "RECORD"
              }
            ],
            "mode": "NULLABLE",
            "name": "jobGetQueryResultsResponse",
            "type": "RECORD"
          },
          {
            "fields": [
              {
                "fields": [
                  {
                    "fields": [
                      {
                        "mode": "NULLABLE",
                        "name": "projectId",
                        "type": "STRING"
                      },
                      {
                        "mode": "NULLABLE",
                        "name": "jobId",
                        "type": "STRING"
                      },
                      {
                        "mode": "NULLABLE",
                        "name": "location",
                        "type": "STRING"
                      }
                    ],
                    "mode": "NULLABLE",
                    "name": "jobName",
                    "type": "RECORD"
                  },
                  {
                    "fields": [
                      {
                        "fields": [
                          {
                            "mode": "NULLABLE",
                            "name": "query",
                            "type": "STRING"
                          },
                          {
                            "fields": [
                              {
                                "mode": "NULLABLE",
                                "name": "projectId",
                                "type": "STRING"
                              },
                              {
                                "mode": "NULLABLE",
                                "name": "datasetId",
                                "type": "STRING"
                              },
                              {
                                "mode": "NULLABLE",
                                "name": "tableId",
                                "type": "STRING"
                              }
                            ],
                            "mode": "NULLABLE",
                            "name": "destinationTable",
                            "type": "RECORD"
                          },
                          {
                            "mode": "NULLABLE",
                            "name": "createDisposition",
                            "type": "STRING"
                          },
                          {
                            "mode": "NULLABLE",
                            "name": "writeDisposition",
                            "type": "STRING"
                          },
                          {
                            "fields": [
                              {
                                "mode": "NULLABLE",
                                "name": "projectId",
                                "type": "STRING"
                              },
                              {
                                "mode": "NULLABLE",
                                "name": "datasetId",
                                "type": "STRING"
                              }
                            ],
                            "mode": "NULLABLE",
                            "name": "defaultDataset",
                            "type": "RECORD"
                          },
                          {
                            "fields": [
                              {
                                "mode": "NULLABLE",
                                "name": "name",
                                "type": "STRING"
                              },
                              {
                                "mode": "REPEATED",
                                "name": "sourceUris",
                                "type": "STRING"
                              }
                            ],
                            "mode": "REPEATED",
                            "name": "tableDefinitions",
                            "type": "RECORD"
                          },
                          {
                            "mode": "NULLABLE",
                            "name": "queryPriority",
                            "type": "STRING"
                          },
                          {
                            "fields": [
                              {
                                "mode": "NULLABLE",
                                "name": "kmsKeyName",
                                "type": "STRING"
                              }
                            ],
                            "mode": "NULLABLE",
                            "name": "destinationTableEncryption",
                            "type": "RECORD"
                          },
                          {
                            "mode": "NULLABLE",
                            "name": "statementType",
                            "type": "STRING"
                          }
                        ],
                        "mode": "NULLABLE",
                        "name": "query",
                        "type": "RECORD"
                      },
                      {
                        "fields": [
                          {
                            "mode": "REPEATED",
                            "name": "sourceUris",
                            "type": "STRING"
                          },
                          {
                            "mode": "NULLABLE",
                            "name": "schemaJson",
                            "type": "STRING"
                          },
                          {
                            "fields": [
                              {
                                "mode": "NULLABLE",
                                "name": "projectId",
                                "type": "STRING"
                              },
                              {
                                "mode": "NULLABLE",
                                "name": "datasetId",
                                "type": "STRING"
                              },
                              {
                                "mode": "NULLABLE",
                                "name": "tableId",
                                "type": "STRING"
                              }
                            ],
                            "mode": "NULLABLE",
                            "name": "destinationTable",
                            "type": "RECORD"
                          },
                          {
                            "mode": "NULLABLE",
                            "name": "createDisposition",
                            "type": "STRING"
                          },
                          {
                            "mode": "NULLABLE",
                            "name": "writeDisposition",
                            "type": "STRING"
                          },
                          {
                            "fields": [
                              {
                                "mode": "NULLABLE",
                                "name": "kmsKeyName",
                                "type": "STRING"
                              }
                            ],
                            "mode": "NULLABLE",
                            "name": "destinationTableEncryption",
                            "type": "RECORD"
                          }
                        ],
                        "mode": "NULLABLE",
                        "name": "load",
                        "type": "RECORD"
                      },
                      {
                        "fields": [
                          {
                            "mode": "REPEATED",
                            "name": "destinationUris",
                            "type": "STRING"
                          },
                          {
                            "fields": [
                              {
                                "mode": "NULLABLE",
                                "name": "projectId",
                                "type": "STRING"
                              },
                              {
                                "mode": "NULLABLE",
                                "name": "datasetId",
                                "type": "STRING"
                              },
                              {
                                "mode": "NULLABLE",
                                "name": "tableId",
                                "type": "STRING"
                              }
                            ],
                            "mode": "NULLABLE",
                            "name": "sourceTable",
                            "type": "RECORD"
                          }
                        ],
                        "mode": "NULLABLE",
                        "name": "extract",
                        "type": "RECORD"
                      },
                      {
                        "fields": [
                          {
                            "fields": [
                              {
                                "mode": "NULLABLE",
                                "name": "projectId",
                                "type": "STRING"
                              },
                              {
                                "mode": "NULLABLE",
                                "name": "datasetId",
                                "type": "STRING"
                              },
                              {
                                "mode": "NULLABLE",
                                "name": "tableId",
                                "type": "STRING"
                              }
                            ],
                            "mode": "REPEATED",
                            "name": "sourceTables",
                            "type": "RECORD"
                          },
                          {
                            "fields": [
                              {
                                "mode": "NULLABLE",
                                "name": "projectId",
                                "type": "STRING"
                              },
                              {
                                "mode": "NULLABLE",
                                "name": "datasetId",
                                "type": "STRING"
                              },
                              {
                                "mode": "NULLABLE",
                                "name": "tableId",
                                "type": "STRING"
                              }
                            ],
                            "mode": "NULLABLE",
                            "name": "destinationTable",
                            "type": "RECORD"
                          },
                          {
                            "mode": "NULLABLE",
                            "name": "createDisposition",
                            "type": "STRING"
                          },
                          {
                            "mode": "NULLABLE",
                            "name": "writeDisposition",
                            "type": "STRING"
                          },
                          {
                            "fields": [
                              {
                                "mode": "NULLABLE",
                                "name": "kmsKeyName",
                                "type": "STRING"
                              }
                            ],
                            "mode": "NULLABLE",
                            "name": "destinationTableEncryption",
                            "type": "RECORD"
                          }
                        ],
                        "mode": "NULLABLE",
                        "name": "tableCopy",
                        "type": "RECORD"
                      },
                      {
                        "mode": "NULLABLE",
                        "name": "dryRun",
                        "type": "BOOLEAN"
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
                      }
                    ],
                    "mode": "NULLABLE",
                    "name": "jobConfiguration",
                    "type": "RECORD"
                  },
                  {
                    "fields": [
                      {
                        "mode": "NULLABLE",
                        "name": "state",
                        "type": "STRING"
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
                        "name": "error",
                        "type": "RECORD"
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
                        "mode": "REPEATED",
                        "name": "additionalErrors",
                        "type": "RECORD"
                      }
                    ],
                    "mode": "NULLABLE",
                    "name": "jobStatus",
                    "type": "RECORD"
                  },
                  {
                    "fields": [
                      {
                        "mode": "NULLABLE",
                        "name": "createTime",
                        "type": "TIMESTAMP"
                      },
                      {
                        "mode": "NULLABLE",
                        "name": "startTime",
                        "type": "TIMESTAMP"
                      },
                      {
                        "mode": "NULLABLE",
                        "name": "endTime",
                        "type": "TIMESTAMP"
                      },
                      {
                        "mode": "NULLABLE",
                        "name": "totalProcessedBytes",
                        "type": "INTEGER"
                      },
                      {
                        "mode": "NULLABLE",
                        "name": "totalBilledBytes",
                        "type": "INTEGER"
                      },
                      {
                        "mode": "NULLABLE",
                        "name": "billingTier",
                        "type": "INTEGER"
                      },
                      {
                        "mode": "NULLABLE",
                        "name": "totalSlotMs",
                        "type": "INTEGER"
                      },
                      {
                        "fields": [
                          {
                            "mode": "NULLABLE",
                            "name": "name",
                            "type": "STRING"
                          },
                          {
                            "mode": "NULLABLE",
                            "name": "slotMs",
                            "type": "INTEGER"
                          }
                        ],
                        "mode": "REPEATED",
                        "name": "reservationUsage",
                        "type": "RECORD"
                      },
                      {
                        "mode": "NULLABLE",
                        "name": "reservation",
                        "type": "STRING"
                      },
                      {
                        "fields": [
                          {
                            "mode": "NULLABLE",
                            "name": "projectId",
                            "type": "STRING"
                          },
                          {
                            "mode": "NULLABLE",
                            "name": "datasetId",
                            "type": "STRING"
                          },
                          {
                            "mode": "NULLABLE",
                            "name": "tableId",
                            "type": "STRING"
                          }
                        ],
                        "mode": "REPEATED",
                        "name": "referencedTables",
                        "type": "RECORD"
                      },
                      {
                        "mode": "NULLABLE",
                        "name": "totalTablesProcessed",
                        "type": "INTEGER"
                      },
                      {
                        "fields": [
                          {
                            "mode": "NULLABLE",
                            "name": "projectId",
                            "type": "STRING"
                          },
                          {
                            "mode": "NULLABLE",
                            "name": "datasetId",
                            "type": "STRING"
                          },
                          {
                            "mode": "NULLABLE",
                            "name": "tableId",
                            "type": "STRING"
                          }
                        ],
                        "mode": "REPEATED",
                        "name": "referencedViews",
                        "type": "RECORD"
                      },
                      {
                        "mode": "NULLABLE",
                        "name": "totalViewsProcessed",
                        "type": "INTEGER"
                      },
                      {
                        "mode": "NULLABLE",
                        "name": "queryOutputRowCount",
                        "type": "INTEGER"
                      },
                      {
                        "mode": "NULLABLE",
                        "name": "totalLoadOutputBytes",
                        "type": "INTEGER"
                      }
                    ],
                    "mode": "NULLABLE",
                    "name": "jobStatistics",
                    "type": "RECORD"
                  }
                ],
                "mode": "NULLABLE",
                "name": "job",
                "type": "RECORD"
              }
            ],
            "mode": "NULLABLE",
            "name": "jobQueryDoneResponse",
            "type": "RECORD"
          },
          {
            "fields": [
              {
                "mode": "NULLABLE",
                "name": "version",
                "type": "INTEGER"
              },
              {
                "fields": [
                  {
                    "mode": "NULLABLE",
                    "name": "role",
                    "type": "STRING"
                  },
                  {
                    "mode": "REPEATED",
                    "name": "members",
                    "type": "STRING"
                  },
                  {
                    "fields": [
                      {
                        "mode": "NULLABLE",
                        "name": "expression",
                        "type": "STRING"
                      },
                      {
                        "mode": "NULLABLE",
                        "name": "title",
                        "type": "STRING"
                      },
                      {
                        "mode": "NULLABLE",
                        "name": "description",
                        "type": "STRING"
                      },
                      {
                        "mode": "NULLABLE",
                        "name": "location",
                        "type": "STRING"
                      }
                    ],
                    "mode": "NULLABLE",
                    "name": "condition",
                    "type": "RECORD"
                  }
                ],
                "mode": "REPEATED",
                "name": "bindings",
                "type": "RECORD"
              },
              {
                "fields": [
                  {
                    "mode": "NULLABLE",
                    "name": "service",
                    "type": "STRING"
                  },
                  {
                    "fields": [
                      {
                        "mode": "NULLABLE",
                        "name": "logType",
                        "type": "STRING"
                      },
                      {
                        "mode": "REPEATED",
                        "name": "exemptedMembers",
                        "type": "STRING"
                      }
                    ],
                    "mode": "REPEATED",
                    "name": "auditLogConfigs",
                    "type": "RECORD"
                  }
                ],
                "mode": "REPEATED",
                "name": "auditConfigs",
                "type": "RECORD"
              },
              {
                "mode": "NULLABLE",
                "name": "etag",
                "type": "STRING"
              }
            ],
            "mode": "NULLABLE",
            "name": "policyResponse",
            "type": "RECORD"
          },
          {
            "fields": [
              {
                "mode": "NULLABLE",
                "name": "eventName",
                "type": "STRING"
              },
              {
                "fields": [
                  {
                    "fields": [
                      {
                        "mode": "NULLABLE",
                        "name": "projectId",
                        "type": "STRING"
                      },
                      {
                        "mode": "NULLABLE",
                        "name": "jobId",
                        "type": "STRING"
                      },
                      {
                        "mode": "NULLABLE",
                        "name": "location",
                        "type": "STRING"
                      }
                    ],
                    "mode": "NULLABLE",
                    "name": "jobName",
                    "type": "RECORD"
                  },
                  {
                    "fields": [
                      {
                        "fields": [
                          {
                            "mode": "NULLABLE",
                            "name": "query",
                            "type": "STRING"
                          },
                          {
                            "fields": [
                              {
                                "mode": "NULLABLE",
                                "name": "projectId",
                                "type": "STRING"
                              },
                              {
                                "mode": "NULLABLE",
                                "name": "datasetId",
                                "type": "STRING"
                              },
                              {
                                "mode": "NULLABLE",
                                "name": "tableId",
                                "type": "STRING"
                              }
                            ],
                            "mode": "NULLABLE",
                            "name": "destinationTable",
                            "type": "RECORD"
                          },
                          {
                            "mode": "NULLABLE",
                            "name": "createDisposition",
                            "type": "STRING"
                          },
                          {
                            "mode": "NULLABLE",
                            "name": "writeDisposition",
                            "type": "STRING"
                          },
                          {
                            "fields": [
                              {
                                "mode": "NULLABLE",
                                "name": "projectId",
                                "type": "STRING"
                              },
                              {
                                "mode": "NULLABLE",
                                "name": "datasetId",
                                "type": "STRING"
                              }
                            ],
                            "mode": "NULLABLE",
                            "name": "defaultDataset",
                            "type": "RECORD"
                          },
                          {
                            "fields": [
                              {
                                "mode": "NULLABLE",
                                "name": "name",
                                "type": "STRING"
                              },
                              {
                                "mode": "REPEATED",
                                "name": "sourceUris",
                                "type": "STRING"
                              }
                            ],
                            "mode": "REPEATED",
                            "name": "tableDefinitions",
                            "type": "RECORD"
                          },
                          {
                            "mode": "NULLABLE",
                            "name": "queryPriority",
                            "type": "STRING"
                          },
                          {
                            "fields": [
                              {
                                "mode": "NULLABLE",
                                "name": "kmsKeyName",
                                "type": "STRING"
                              }
                            ],
                            "mode": "NULLABLE",
                            "name": "destinationTableEncryption",
                            "type": "RECORD"
                          },
                          {
                            "mode": "NULLABLE",
                            "name": "statementType",
                            "type": "STRING"
                          }
                        ],
                        "mode": "NULLABLE",
                        "name": "query",
                        "type": "RECORD"
                      },
                      {
                        "fields": [
                          {
                            "mode": "REPEATED",
                            "name": "sourceUris",
                            "type": "STRING"
                          },
                          {
                            "mode": "NULLABLE",
                            "name": "schemaJson",
                            "type": "STRING"
                          },
                          {
                            "fields": [
                              {
                                "mode": "NULLABLE",
                                "name": "projectId",
                                "type": "STRING"
                              },
                              {
                                "mode": "NULLABLE",
                                "name": "datasetId",
                                "type": "STRING"
                              },
                              {
                                "mode": "NULLABLE",
                                "name": "tableId",
                                "type": "STRING"
                              }
                            ],
                            "mode": "NULLABLE",
                            "name": "destinationTable",
                            "type": "RECORD"
                          },
                          {
                            "mode": "NULLABLE",
                            "name": "createDisposition",
                            "type": "STRING"
                          },
                          {
                            "mode": "NULLABLE",
                            "name": "writeDisposition",
                            "type": "STRING"
                          },
                          {
                            "fields": [
                              {
                                "mode": "NULLABLE",
                                "name": "kmsKeyName",
                                "type": "STRING"
                              }
                            ],
                            "mode": "NULLABLE",
                            "name": "destinationTableEncryption",
                            "type": "RECORD"
                          }
                        ],
                        "mode": "NULLABLE",
                        "name": "load",
                        "type": "RECORD"
                      },
                      {
                        "fields": [
                          {
                            "mode": "REPEATED",
                            "name": "destinationUris",
                            "type": "STRING"
                          },
                          {
                            "fields": [
                              {
                                "mode": "NULLABLE",
                                "name": "projectId",
                                "type": "STRING"
                              },
                              {
                                "mode": "NULLABLE",
                                "name": "datasetId",
                                "type": "STRING"
                              },
                              {
                                "mode": "NULLABLE",
                                "name": "tableId",
                                "type": "STRING"
                              }
                            ],
                            "mode": "NULLABLE",
                            "name": "sourceTable",
                            "type": "RECORD"
                          }
                        ],
                        "mode": "NULLABLE",
                        "name": "extract",
                        "type": "RECORD"
                      },
                      {
                        "fields": [
                          {
                            "fields": [
                              {
                                "mode": "NULLABLE",
                                "name": "projectId",
                                "type": "STRING"
                              },
                              {
                                "mode": "NULLABLE",
                                "name": "datasetId",
                                "type": "STRING"
                              },
                              {
                                "mode": "NULLABLE",
                                "name": "tableId",
                                "type": "STRING"
                              }
                            ],
                            "mode": "REPEATED",
                            "name": "sourceTables",
                            "type": "RECORD"
                          },
                          {
                            "fields": [
                              {
                                "mode": "NULLABLE",
                                "name": "projectId",
                                "type": "STRING"
                              },
                              {
                                "mode": "NULLABLE",
                                "name": "datasetId",
                                "type": "STRING"
                              },
                              {
                                "mode": "NULLABLE",
                                "name": "tableId",
                                "type": "STRING"
                              }
                            ],
                            "mode": "NULLABLE",
                            "name": "destinationTable",
                            "type": "RECORD"
                          },
                          {
                            "mode": "NULLABLE",
                            "name": "createDisposition",
                            "type": "STRING"
                          },
                          {
                            "mode": "NULLABLE",
                            "name": "writeDisposition",
                            "type": "STRING"
                          },
                          {
                            "fields": [
                              {
                                "mode": "NULLABLE",
                                "name": "kmsKeyName",
                                "type": "STRING"
                              }
                            ],
                            "mode": "NULLABLE",
                            "name": "destinationTableEncryption",
                            "type": "RECORD"
                          }
                        ],
                        "mode": "NULLABLE",
                        "name": "tableCopy",
                        "type": "RECORD"
                      },
                      {
                        "mode": "NULLABLE",
                        "name": "dryRun",
                        "type": "BOOLEAN"
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
                      }
                    ],
                    "mode": "NULLABLE",
                    "name": "jobConfiguration",
                    "type": "RECORD"
                  },
                  {
                    "fields": [
                      {
                        "mode": "NULLABLE",
                        "name": "state",
                        "type": "STRING"
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
                        "name": "error",
                        "type": "RECORD"
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
                        "mode": "REPEATED",
                        "name": "additionalErrors",
                        "type": "RECORD"
                      }
                    ],
                    "mode": "NULLABLE",
                    "name": "jobStatus",
                    "type": "RECORD"
                  },
                  {
                    "fields": [
                      {
                        "mode": "NULLABLE",
                        "name": "createTime",
                        "type": "TIMESTAMP"
                      },
                      {
                        "mode": "NULLABLE",
                        "name": "startTime",
                        "type": "TIMESTAMP"
                      },
                      {
                        "mode": "NULLABLE",
                        "name": "endTime",
                        "type": "TIMESTAMP"
                      },
                      {
                        "mode": "NULLABLE",
                        "name": "totalProcessedBytes",
                        "type": "INTEGER"
                      },
                      {
                        "mode": "NULLABLE",
                        "name": "totalBilledBytes",
                        "type": "INTEGER"
                      },
                      {
                        "mode": "NULLABLE",
                        "name": "billingTier",
                        "type": "INTEGER"
                      },
                      {
                        "mode": "NULLABLE",
                        "name": "totalSlotMs",
                        "type": "INTEGER"
                      },
                      {
                        "fields": [
                          {
                            "mode": "NULLABLE",
                            "name": "name",
                            "type": "STRING"
                          },
                          {
                            "mode": "NULLABLE",
                            "name": "slotMs",
                            "type": "INTEGER"
                          }
                        ],
                        "mode": "REPEATED",
                        "name": "reservationUsage",
                        "type": "RECORD"
                      },
                      {
                        "mode": "NULLABLE",
                        "name": "reservation",
                        "type": "STRING"
                      },
                      {
                        "fields": [
                          {
                            "mode": "NULLABLE",
                            "name": "projectId",
                            "type": "STRING"
                          },
                          {
                            "mode": "NULLABLE",
                            "name": "datasetId",
                            "type": "STRING"
                          },
                          {
                            "mode": "NULLABLE",
                            "name": "tableId",
                            "type": "STRING"
                          }
                        ],
                        "mode": "REPEATED",
                        "name": "referencedTables",
                        "type": "RECORD"
                      },
                      {
                        "mode": "NULLABLE",
                        "name": "totalTablesProcessed",
                        "type": "INTEGER"
                      },
                      {
                        "fields": [
                          {
                            "mode": "NULLABLE",
                            "name": "projectId",
                            "type": "STRING"
                          },
                          {
                            "mode": "NULLABLE",
                            "name": "datasetId",
                            "type": "STRING"
                          },
                          {
                            "mode": "NULLABLE",
                            "name": "tableId",
                            "type": "STRING"
                          }
                        ],
                        "mode": "REPEATED",
                        "name": "referencedViews",
                        "type": "RECORD"
                      },
                      {
                        "mode": "NULLABLE",
                        "name": "totalViewsProcessed",
                        "type": "INTEGER"
                      },
                      {
                        "mode": "NULLABLE",
                        "name": "queryOutputRowCount",
                        "type": "INTEGER"
                      },
                      {
                        "mode": "NULLABLE",
                        "name": "totalLoadOutputBytes",
                        "type": "INTEGER"
                      }
                    ],
                    "mode": "NULLABLE",
                    "name": "jobStatistics",
                    "type": "RECORD"
                  }
                ],
                "mode": "NULLABLE",
                "name": "job",
                "type": "RECORD"
              }
            ],
            "mode": "NULLABLE",
            "name": "jobCompletedEvent",
            "type": "RECORD"
          },
          {
            "fields": [
              {
                "fields": [
                  {
                    "mode": "NULLABLE",
                    "name": "projectId",
                    "type": "STRING"
                  },
                  {
                    "mode": "NULLABLE",
                    "name": "datasetId",
                    "type": "STRING"
                  },
                  {
                    "mode": "NULLABLE",
                    "name": "tableId",
                    "type": "STRING"
                  }
                ],
                "mode": "NULLABLE",
                "name": "tableName",
                "type": "RECORD"
              },
              {
                "mode": "REPEATED",
                "name": "referencedFields",
                "type": "STRING"
              }
            ],
            "mode": "REPEATED",
            "name": "tableDataReadEvents",
            "type": "RECORD"
          }
        ],
        "mode": "NULLABLE",
        "name": "servicedata_v1_bigquery",
        "type": "RECORD"
      },
      {
        "mode": "NULLABLE",
        "name": "requestJson",
        "type": "STRING"
      },
      {
        "mode": "NULLABLE",
        "name": "metadataJson",
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
        "name": "authorization_k8s_io_decision",
        "type": "STRING"
      },
      {
        "mode": "NULLABLE",
        "name": "authorization_k8s_io_reason",
        "type": "STRING"
      },
      {
        "mode": "NULLABLE",
        "name": "authentication_kubernetes_io_credential_id",
        "type": "STRING"
      },
      {
        "mode": "NULLABLE",
        "name": "audit_k8s_io_truncated",
        "type": "STRING"
      },
      {
        "mode": "NULLABLE",
        "name": "apiserver_latency_k8s_io_total",
        "type": "STRING"
      },
      {
        "mode": "NULLABLE",
        "name": "apiserver_latency_k8s_io_apf_queue_wait",
        "type": "STRING"
      },
      {
        "mode": "NULLABLE",
        "name": "apiserver_latency_k8s_io_transform_response_object",
        "type": "STRING"
      },
      {
        "mode": "NULLABLE",
        "name": "apiserver_latency_k8s_io_serialize_response_object",
        "type": "STRING"
      },
      {
        "mode": "NULLABLE",
        "name": "apiserver_latency_k8s_io_response_write",
        "type": "STRING"
      },
      {
        "mode": "NULLABLE",
        "name": "apiserver_latency_k8s_io_etcd",
        "type": "STRING"
      },
      {
        "mode": "NULLABLE",
        "name": "apiserver_latency_k8s_io_validating_webhook",
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