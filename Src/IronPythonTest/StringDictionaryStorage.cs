// Licensed to the .NET Foundation under one or more agreements.
// The .NET Foundation licenses this file to you under the Apache 2.0 License.
// See the LICENSE file in the project root for more information.

using System;
using System.Collections;
using System.Collections.Generic;
using System.Threading;

using Microsoft.Scripting.Runtime;

using IronPython.Runtime;

namespace IronPythonTest {
    [Serializable]
    internal class StringDictionaryStorage : DictionaryStorage {
        private readonly IDictionary<string, object>/*!*/ _dict; // the underlying dictionary
        private Dictionary<object, object> _objDict;

        public StringDictionaryStorage(IDictionary<string, object>/*!*/ dict) {
            _dict = dict;
        }

        public StringDictionaryStorage(IDictionary<string, object> dict, Dictionary<object, object> objDict) {
            _dict = dict;
            _objDict = objDict;
        }

        public override void Add(ref DictionaryStorage storage, object key, object value) {
            lock (this) {
                string strKey = key as string;
                if (strKey != null) {
                    _dict[strKey] = value;
                } else {
                    EnsureObjectDictionary();
                    _objDict[CustomStringDictionary.NullToObj(key)] = value;
                }
            }
        }

        public override bool Contains(object key) {
            lock (this) {
                string strKey = key as string;
                if (strKey != null) {
                    return _dict.ContainsKey(strKey);
                }

                if (_objDict != null) {
                    return _objDict.ContainsKey(CustomStringDictionary.NullToObj(key));
                }

                return false;
            }
        }

        public override bool Remove(ref DictionaryStorage storage, object key) {
            lock (this) {
                string strKey = key as string;
                if (strKey != null) {
                    return _dict.Remove(strKey);
                }

                if (_objDict != null) {
                    return _objDict.Remove(CustomStringDictionary.NullToObj(key));
                }

                return false;
            }
        }

        public override DictionaryStorage AsMutable(ref DictionaryStorage storage) => this;

        public override bool TryGetValue(object key, out object value) {
            lock (this) {
                string strKey = key as string;
                if (strKey != null) {
                    return _dict.TryGetValue(strKey, out value);
                }

                if (_objDict != null) {
                    return _objDict.TryGetValue(CustomStringDictionary.NullToObj(key), out value);
                }

                value = null;
                return false;
            }
        }

        public override int Count {
            get {
                lock (this) {
                    int count = _dict.Count;
                    if (_objDict != null) {
                        count += _objDict.Count;
                    }
                    return count;
                }
            }
        }

        public override void Clear(ref DictionaryStorage storage) {
            lock (this) {
                _dict.Clear();
                _objDict?.Clear();
            }
        }

        public override List<KeyValuePair<object, object>> GetItems() {
            List<KeyValuePair<object, object>> res = new List<KeyValuePair<object, object>>();
            lock (this) {
                foreach (KeyValuePair<string, object> kvp in _dict) {
                    res.Add(new KeyValuePair<object, object>(kvp.Key, kvp.Value));
                }

                if (_objDict != null) {
                    foreach (KeyValuePair<object, object> kvp in _objDict) {
                        res.Add(kvp);
                    }
                }
            }
            return res;
        }
        
        public override DictionaryStorage Clone() {
            lock (this) {
                IDictionary<string, object> dict;
                ICloneable cloneable = _dict as ICloneable;
                if (cloneable != null) {
                    dict = (IDictionary<string, object>)cloneable.Clone();
                } else {
                    dict = new Dictionary<string, object>(_dict, StringComparer.Ordinal);
                }

                Dictionary<object, object> objDict = null;
                if (_objDict != null) {
                    objDict = new Dictionary<object, object>(_objDict, DefaultContext.DefaultPythonContext.EqualityComparer);
                }

                return new StringDictionaryStorage(dict, objDict);
            }
        }

        private void EnsureObjectDictionary() {
            if (_objDict == null) {
                Interlocked.CompareExchange<Dictionary<object, object>>(ref _objDict, new Dictionary<object, object>(DefaultContext.DefaultPythonContext.EqualityComparer), null);
            }            
        }
    }
}
