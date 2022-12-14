# Licensed to the .NET Foundation under one or more agreements.
# The .NET Foundation licenses this file to you under the Apache 2.0 License.
# See the LICENSE file in the project root for more information.

##
## Run selected tests from sqlite3.test from StdLib
##

import unittest
import sys

from iptest import is_linux, is_netcoreapp21, run_test

if is_netcoreapp21: raise SystemExit # no IronPython.SQLite.dll with .NET Core 2.1

import sqlite3.test.dbapi
import sqlite3.test.dump
import sqlite3.test.factory
import sqlite3.test.hooks
import sqlite3.test.regression
import sqlite3.test.transactions
import sqlite3.test.types
import sqlite3.test.userfunctions

def load_tests(loader, standard_tests, pattern):
    if sys.implementation.name == 'ironpython':
        suite = unittest.TestSuite()
        suite.addTest(sqlite3.test.dbapi.ModuleTests('CheckAPILevel'))
        suite.addTest(sqlite3.test.dbapi.ModuleTests('CheckDataError'))
        suite.addTest(sqlite3.test.dbapi.ModuleTests('CheckDatabaseError'))
        suite.addTest(sqlite3.test.dbapi.ModuleTests('CheckError'))
        suite.addTest(sqlite3.test.dbapi.ModuleTests('CheckIntegrityError'))
        suite.addTest(sqlite3.test.dbapi.ModuleTests('CheckInterfaceError'))
        suite.addTest(sqlite3.test.dbapi.ModuleTests('CheckInternalError'))
        suite.addTest(sqlite3.test.dbapi.ModuleTests('CheckNotSupportedError'))
        suite.addTest(sqlite3.test.dbapi.ModuleTests('CheckOperationalError'))
        suite.addTest(sqlite3.test.dbapi.ModuleTests('CheckParamStyle'))
        suite.addTest(sqlite3.test.dbapi.ModuleTests('CheckProgrammingError'))
        suite.addTest(sqlite3.test.dbapi.ModuleTests('CheckThreadSafety'))
        suite.addTest(sqlite3.test.dbapi.ModuleTests('CheckWarning'))
        suite.addTest(sqlite3.test.dbapi.ConnectionTests('CheckClose'))
        suite.addTest(sqlite3.test.dbapi.ConnectionTests('CheckCommit'))
        suite.addTest(sqlite3.test.dbapi.ConnectionTests('CheckCommitAfterNoChanges'))
        suite.addTest(sqlite3.test.dbapi.ConnectionTests('CheckCursor'))
        suite.addTest(sqlite3.test.dbapi.ConnectionTests('CheckExceptions'))
        suite.addTest(sqlite3.test.dbapi.ConnectionTests('CheckFailedOpen'))
        suite.addTest(unittest.expectedFailure(sqlite3.test.dbapi.ConnectionTests('CheckInTransaction')))
        suite.addTest(sqlite3.test.dbapi.ConnectionTests('CheckInTransactionRO'))
        #suite.addTest(unittest.expectedFailure(sqlite3.test.dbapi.ConnectionTests('CheckOpenUri')))
        suite.addTest(sqlite3.test.dbapi.ConnectionTests('CheckRollback'))
        suite.addTest(sqlite3.test.dbapi.ConnectionTests('CheckRollbackAfterNoChanges'))
        suite.addTest(sqlite3.test.dbapi.CursorTests('CheckArraySize'))
        suite.addTest(sqlite3.test.dbapi.CursorTests('CheckClose'))
        suite.addTest(sqlite3.test.dbapi.CursorTests('CheckCursorConnection'))
        suite.addTest(sqlite3.test.dbapi.CursorTests('CheckCursorWrongClass'))
        suite.addTest(sqlite3.test.dbapi.CursorTests('CheckExecuteArgFloat'))
        suite.addTest(sqlite3.test.dbapi.CursorTests('CheckExecuteArgInt'))
        suite.addTest(sqlite3.test.dbapi.CursorTests('CheckExecuteArgString'))
        suite.addTest(unittest.expectedFailure(sqlite3.test.dbapi.CursorTests('CheckExecuteArgStringWithZeroByte')))
        suite.addTest(sqlite3.test.dbapi.CursorTests('CheckExecuteDictMapping'))
        suite.addTest(sqlite3.test.dbapi.CursorTests('CheckExecuteDictMappingNoArgs'))
        suite.addTest(sqlite3.test.dbapi.CursorTests('CheckExecuteDictMappingTooLittleArgs'))
        suite.addTest(sqlite3.test.dbapi.CursorTests('CheckExecuteDictMappingUnnamed'))
        suite.addTest(unittest.expectedFailure(sqlite3.test.dbapi.CursorTests('CheckExecuteDictMapping_Mapping')))
        suite.addTest(sqlite3.test.dbapi.CursorTests('CheckExecuteIllegalSql'))
        suite.addTest(sqlite3.test.dbapi.CursorTests('CheckExecuteManyGenerator'))
        suite.addTest(unittest.expectedFailure(sqlite3.test.dbapi.CursorTests('CheckExecuteManyIterator')))
        suite.addTest(sqlite3.test.dbapi.CursorTests('CheckExecuteManyNotIterable'))
        suite.addTest(sqlite3.test.dbapi.CursorTests('CheckExecuteManySelect'))
        suite.addTest(sqlite3.test.dbapi.CursorTests('CheckExecuteManySequence'))
        suite.addTest(sqlite3.test.dbapi.CursorTests('CheckExecuteManyWrongSqlArg'))
        suite.addTest(sqlite3.test.dbapi.CursorTests('CheckExecuteNoArgs'))
        suite.addTest(sqlite3.test.dbapi.CursorTests('CheckExecuteParamList'))
        suite.addTest(unittest.expectedFailure(sqlite3.test.dbapi.CursorTests('CheckExecuteParamSequence')))
        suite.addTest(unittest.expectedFailure(sqlite3.test.dbapi.CursorTests('CheckExecuteTooMuchSql')))
        suite.addTest(sqlite3.test.dbapi.CursorTests('CheckExecuteTooMuchSql2'))
        suite.addTest(sqlite3.test.dbapi.CursorTests('CheckExecuteTooMuchSql3'))
        suite.addTest(sqlite3.test.dbapi.CursorTests('CheckExecuteWrongNoOfArgs1'))
        suite.addTest(sqlite3.test.dbapi.CursorTests('CheckExecuteWrongNoOfArgs2'))
        suite.addTest(sqlite3.test.dbapi.CursorTests('CheckExecuteWrongNoOfArgs3'))
        suite.addTest(sqlite3.test.dbapi.CursorTests('CheckExecuteWrongSqlArg'))
        suite.addTest(sqlite3.test.dbapi.CursorTests('CheckFetchIter'))
        suite.addTest(sqlite3.test.dbapi.CursorTests('CheckFetchall'))
        suite.addTest(sqlite3.test.dbapi.CursorTests('CheckFetchmany'))
        suite.addTest(sqlite3.test.dbapi.CursorTests('CheckFetchmanyKwArg'))
        suite.addTest(sqlite3.test.dbapi.CursorTests('CheckFetchone'))
        suite.addTest(sqlite3.test.dbapi.CursorTests('CheckFetchoneNoStatement'))
        suite.addTest(sqlite3.test.dbapi.CursorTests('CheckRowcountExecute'))
        suite.addTest(sqlite3.test.dbapi.CursorTests('CheckRowcountExecutemany'))
        suite.addTest(sqlite3.test.dbapi.CursorTests('CheckRowcountSelect'))
        suite.addTest(sqlite3.test.dbapi.CursorTests('CheckSetinputsizes'))
        suite.addTest(sqlite3.test.dbapi.CursorTests('CheckSetoutputsize'))
        suite.addTest(sqlite3.test.dbapi.CursorTests('CheckSetoutputsizeNoColumn'))
        suite.addTest(sqlite3.test.dbapi.CursorTests('CheckTotalChanges'))
        suite.addTest(sqlite3.test.dbapi.CursorTests('CheckWrongCursorCallable'))
        suite.addTest(sqlite3.test.dbapi.ThreadTests('CheckConClose'))
        suite.addTest(sqlite3.test.dbapi.ThreadTests('CheckConCommit'))
        suite.addTest(sqlite3.test.dbapi.ThreadTests('CheckConCursor'))
        suite.addTest(sqlite3.test.dbapi.ThreadTests('CheckConRollback'))
        suite.addTest(sqlite3.test.dbapi.ThreadTests('CheckCurClose'))
        suite.addTest(sqlite3.test.dbapi.ThreadTests('CheckCurExecute'))
        suite.addTest(sqlite3.test.dbapi.ThreadTests('CheckCurImplicitBegin'))
        suite.addTest(sqlite3.test.dbapi.ThreadTests('CheckCurIterNext'))
        suite.addTest(sqlite3.test.dbapi.ConstructorTests('CheckBinary'))
        suite.addTest(sqlite3.test.dbapi.ConstructorTests('CheckDate'))
        suite.addTest(sqlite3.test.dbapi.ConstructorTests('CheckDateFromTicks'))
        suite.addTest(sqlite3.test.dbapi.ConstructorTests('CheckTime'))
        suite.addTest(sqlite3.test.dbapi.ConstructorTests('CheckTimeFromTicks'))
        suite.addTest(sqlite3.test.dbapi.ConstructorTests('CheckTimestamp'))
        suite.addTest(sqlite3.test.dbapi.ConstructorTests('CheckTimestampFromTicks'))
        suite.addTest(sqlite3.test.dbapi.ExtensionTests('CheckConnectionExecute'))
        suite.addTest(sqlite3.test.dbapi.ExtensionTests('CheckConnectionExecutemany'))
        suite.addTest(unittest.expectedFailure(sqlite3.test.dbapi.ExtensionTests('CheckConnectionExecutescript')))
        suite.addTest(sqlite3.test.dbapi.ExtensionTests('CheckScriptErrorNormal'))
        suite.addTest(unittest.expectedFailure(sqlite3.test.dbapi.ExtensionTests('CheckScriptStringSql')))
        suite.addTest(unittest.expectedFailure(sqlite3.test.dbapi.ExtensionTests('CheckScriptSyntaxError')))
        suite.addTest(unittest.expectedFailure(sqlite3.test.dbapi.ClosedConTests('CheckClosedCall')))
        suite.addTest(sqlite3.test.dbapi.ClosedConTests('CheckClosedConCommit'))
        suite.addTest(sqlite3.test.dbapi.ClosedConTests('CheckClosedConCursor'))
        suite.addTest(sqlite3.test.dbapi.ClosedConTests('CheckClosedConRollback'))
        suite.addTest(unittest.expectedFailure(sqlite3.test.dbapi.ClosedConTests('CheckClosedCreateAggregate')))
        suite.addTest(unittest.expectedFailure(sqlite3.test.dbapi.ClosedConTests('CheckClosedCreateFunction')))
        suite.addTest(sqlite3.test.dbapi.ClosedConTests('CheckClosedCurExecute'))
        suite.addTest(unittest.expectedFailure(sqlite3.test.dbapi.ClosedConTests('CheckClosedSetAuthorizer')))
        suite.addTest(unittest.expectedFailure(sqlite3.test.dbapi.ClosedConTests('CheckClosedSetProgressCallback')))
        suite.addTest(unittest.expectedFailure(sqlite3.test.dbapi.ClosedCurTests('CheckClosed')))
        suite.addTest(unittest.expectedFailure(sqlite3.test.dump.DumpTests('CheckTableDump')))
        suite.addTest(unittest.expectedFailure(sqlite3.test.dump.DumpTests('CheckUnorderableRow')))
        #suite.addTest(unittest.expectedFailure(sqlite3.test.factory.ConnectionFactoryTests('CheckIsInstance')))
        suite.addTest(unittest.expectedFailure(sqlite3.test.factory.CursorFactoryTests('CheckIsInstance')))
        suite.addTest(unittest.expectedFailure(sqlite3.test.factory.RowFactoryTestsBackwardsCompat('CheckIsProducedByFactory')))
        suite.addTest(sqlite3.test.factory.RowFactoryTests('CheckCustomFactory'))
        suite.addTest(sqlite3.test.factory.RowFactoryTests('CheckFakeCursorClass'))
        suite.addTest(sqlite3.test.factory.RowFactoryTests('CheckSqliteRowAsDict'))
        suite.addTest(unittest.expectedFailure(sqlite3.test.factory.RowFactoryTests('CheckSqliteRowAsSequence')))
        suite.addTest(sqlite3.test.factory.RowFactoryTests('CheckSqliteRowAsTuple'))
        suite.addTest(sqlite3.test.factory.RowFactoryTests('CheckSqliteRowHashCmp'))
        suite.addTest(unittest.expectedFailure(sqlite3.test.factory.RowFactoryTests('CheckSqliteRowIndex')))
        suite.addTest(sqlite3.test.factory.RowFactoryTests('CheckSqliteRowIter'))
        suite.addTest(sqlite3.test.factory.TextFactoryTests('CheckCustom'))
        suite.addTest(sqlite3.test.factory.TextFactoryTests('CheckOptimizedUnicode'))
        suite.addTest(unittest.expectedFailure(sqlite3.test.factory.TextFactoryTests('CheckString')))
        suite.addTest(sqlite3.test.factory.TextFactoryTests('CheckUnicode'))
        suite.addTest(unittest.expectedFailure(sqlite3.test.factory.TextFactoryTestsWithEmbeddedZeroBytes('CheckBytearray')))
        suite.addTest(unittest.expectedFailure(sqlite3.test.factory.TextFactoryTestsWithEmbeddedZeroBytes('CheckBytes')))
        suite.addTest(unittest.expectedFailure(sqlite3.test.factory.TextFactoryTestsWithEmbeddedZeroBytes('CheckCustom')))
        suite.addTest(unittest.expectedFailure(sqlite3.test.factory.TextFactoryTestsWithEmbeddedZeroBytes('CheckString')))
        suite.addTest(unittest.expectedFailure(sqlite3.test.hooks.CollationTests('CheckCollationIsUsed')))
        suite.addTest(unittest.expectedFailure(sqlite3.test.hooks.CollationTests('CheckCollationRegisterTwice')))
        suite.addTest(unittest.expectedFailure(sqlite3.test.hooks.CollationTests('CheckCollationReturnsLargeInteger')))
        suite.addTest(unittest.expectedFailure(sqlite3.test.hooks.CollationTests('CheckCreateCollationNotAscii')))
        suite.addTest(unittest.expectedFailure(sqlite3.test.hooks.CollationTests('CheckCreateCollationNotCallable')))
        suite.addTest(unittest.expectedFailure(sqlite3.test.hooks.CollationTests('CheckDeregisterCollation')))
        suite.addTest(unittest.expectedFailure(sqlite3.test.hooks.ProgressTests('CheckCancelOperation')))
        suite.addTest(unittest.expectedFailure(sqlite3.test.hooks.ProgressTests('CheckClearHandler')))
        suite.addTest(unittest.expectedFailure(sqlite3.test.hooks.ProgressTests('CheckOpcodeCount')))
        suite.addTest(unittest.expectedFailure(sqlite3.test.hooks.ProgressTests('CheckProgressHandlerUsed')))
        suite.addTest(unittest.expectedFailure(sqlite3.test.hooks.TraceCallbackTests('CheckClearTraceCallback')))
        suite.addTest(unittest.expectedFailure(sqlite3.test.hooks.TraceCallbackTests('CheckTraceCallbackUsed')))
        suite.addTest(unittest.expectedFailure(sqlite3.test.hooks.TraceCallbackTests('CheckUnicodeContent')))
        suite.addTest(sqlite3.test.regression.RegressionTests('CheckAutoCommit'))
        suite.addTest(unittest.expectedFailure(sqlite3.test.regression.RegressionTests('CheckCollation')))
        suite.addTest(sqlite3.test.regression.RegressionTests('CheckColumnNameWithSpaces'))
        suite.addTest(unittest.expectedFailure(sqlite3.test.regression.RegressionTests('CheckConnectionCall')))
        suite.addTest(unittest.expectedFailure(sqlite3.test.regression.RegressionTests('CheckConnectionConstructorCallCheck')))
        suite.addTest(unittest.expectedFailure(sqlite3.test.regression.RegressionTests('CheckConvertTimestampMicrosecondPadding')))
        suite.addTest(unittest.expectedFailure(sqlite3.test.regression.RegressionTests('CheckCursorConstructorCallCheck')))
        suite.addTest(unittest.expectedFailure(sqlite3.test.regression.RegressionTests('CheckCursorRegistration')))
        suite.addTest(sqlite3.test.regression.RegressionTests('CheckEmptyStatement'))
        suite.addTest(unittest.expectedFailure(sqlite3.test.regression.RegressionTests('CheckErrorMsgDecodeError')))
        suite.addTest(sqlite3.test.regression.RegressionTests('CheckInvalidIsolationLevelType'))
        suite.addTest(unittest.expectedFailure(sqlite3.test.regression.RegressionTests('CheckNullCharacter')))
        suite.addTest(unittest.expectedFailure(sqlite3.test.regression.RegressionTests('CheckOnConflictRollback')))
        suite.addTest(sqlite3.test.regression.RegressionTests('CheckPragmaAutocommit'))
        suite.addTest(sqlite3.test.regression.RegressionTests('CheckPragmaSchemaVersion'))
        suite.addTest(sqlite3.test.regression.RegressionTests('CheckPragmaUserVersion'))
        suite.addTest(unittest.expectedFailure(sqlite3.test.regression.RegressionTests('CheckRecursiveCursorUse')))
        suite.addTest(sqlite3.test.regression.RegressionTests('CheckRegisterAdapter'))
        suite.addTest(unittest.expectedFailure(sqlite3.test.regression.RegressionTests('CheckSetDict')))
        suite.addTest(sqlite3.test.regression.RegressionTests('CheckSetIsolationLevel'))
        suite.addTest(sqlite3.test.regression.RegressionTests('CheckStatementFinalizationOnCloseDb'))
        suite.addTest(sqlite3.test.regression.RegressionTests('CheckStatementReset'))
        suite.addTest(unittest.expectedFailure(sqlite3.test.regression.RegressionTests('CheckStrSubclass')))
        suite.addTest(unittest.expectedFailure(sqlite3.test.regression.RegressionTests('CheckTypeMapUsage')))
        suite.addTest(sqlite3.test.regression.RegressionTests('CheckWorkaroundForBuggySqliteTransferBindings'))
        suite.addTest(sqlite3.test.transactions.TransactionTests('CheckDMLdoesAutoCommitBefore'))
        suite.addTest(sqlite3.test.transactions.TransactionTests('CheckDeleteStartsTransaction'))
        suite.addTest(sqlite3.test.transactions.TransactionTests('CheckInsertStartsTransaction'))
        if is_linux:
            suite.addTest(unittest.expectedFailure(sqlite3.test.transactions.TransactionTests('CheckLocking')))
            suite.addTest(unittest.expectedFailure(sqlite3.test.transactions.TransactionTests('CheckRaiseTimeout')))
        else:
            suite.addTest(sqlite3.test.transactions.TransactionTests('CheckLocking'))
            suite.addTest(sqlite3.test.transactions.TransactionTests('CheckRaiseTimeout'))
        suite.addTest(sqlite3.test.transactions.TransactionTests('CheckReplaceStartsTransaction'))
        suite.addTest(unittest.expectedFailure(sqlite3.test.transactions.TransactionTests('CheckRollbackCursorConsistency')))
        suite.addTest(sqlite3.test.transactions.TransactionTests('CheckToggleAutoCommit'))
        suite.addTest(sqlite3.test.transactions.TransactionTests('CheckUpdateStartsTransaction'))
        suite.addTest(sqlite3.test.transactions.SpecialCommandTests('CheckDropTable'))
        suite.addTest(sqlite3.test.transactions.SpecialCommandTests('CheckPragma'))
        suite.addTest(sqlite3.test.transactions.SpecialCommandTests('CheckVacuum'))
        suite.addTest(unittest.expectedFailure(sqlite3.test.types.SqliteTypeTests('CheckBlob')))
        suite.addTest(sqlite3.test.types.SqliteTypeTests('CheckFloat'))
        suite.addTest(sqlite3.test.types.SqliteTypeTests('CheckLargeInt'))
        suite.addTest(sqlite3.test.types.SqliteTypeTests('CheckSmallInt'))
        suite.addTest(sqlite3.test.types.SqliteTypeTests('CheckString'))
        suite.addTest(sqlite3.test.types.SqliteTypeTests('CheckUnicodeExecute'))
        suite.addTest(unittest.expectedFailure(sqlite3.test.types.DeclTypesTests('CheckBlob')))
        suite.addTest(sqlite3.test.types.DeclTypesTests('CheckBool'))
        suite.addTest(sqlite3.test.types.DeclTypesTests('CheckFloat'))
        suite.addTest(sqlite3.test.types.DeclTypesTests('CheckFoo'))
        suite.addTest(sqlite3.test.types.DeclTypesTests('CheckLargeInt'))
        suite.addTest(sqlite3.test.types.DeclTypesTests('CheckNumber1'))
        suite.addTest(sqlite3.test.types.DeclTypesTests('CheckNumber2'))
        suite.addTest(sqlite3.test.types.DeclTypesTests('CheckSmallInt'))
        suite.addTest(sqlite3.test.types.DeclTypesTests('CheckString'))
        suite.addTest(sqlite3.test.types.DeclTypesTests('CheckUnicode'))
        suite.addTest(sqlite3.test.types.DeclTypesTests('CheckUnsupportedDict'))
        suite.addTest(sqlite3.test.types.DeclTypesTests('CheckUnsupportedSeq'))
        suite.addTest(sqlite3.test.types.ColNamesTests('CheckCaseInConverterName'))
        suite.addTest(unittest.expectedFailure(sqlite3.test.types.ColNamesTests('CheckColName')))
        suite.addTest(sqlite3.test.types.ColNamesTests('CheckCursorDescriptionNoRow'))
        suite.addTest(sqlite3.test.types.ColNamesTests('CheckDeclTypeNotUsed'))
        suite.addTest(sqlite3.test.types.ColNamesTests('CheckNone'))
        suite.addTest(unittest.expectedFailure(sqlite3.test.types.ObjectAdaptationTests('CheckCasterIsUsed')))
        suite.addTest(unittest.expectedFailure(sqlite3.test.types.BinaryConverterTests('CheckBinaryInputForConverter')))
        suite.addTest(unittest.expectedFailure(sqlite3.test.types.DateTimeTests('CheckDateTimeSubSeconds')))
        suite.addTest(unittest.expectedFailure(sqlite3.test.types.DateTimeTests('CheckDateTimeSubSecondsFloatingPoint')))
        suite.addTest(unittest.expectedFailure(sqlite3.test.types.DateTimeTests('CheckSqlTimestamp')))
        suite.addTest(unittest.expectedFailure(sqlite3.test.types.DateTimeTests('CheckSqliteDate')))
        suite.addTest(unittest.expectedFailure(sqlite3.test.types.DateTimeTests('CheckSqliteTimestamp')))
        #suite.addTest(unittest.expectedFailure(sqlite3.test.userfunctions.AuthorizerIllegalTypeTests('test_column_access')))
        #suite.addTest(unittest.expectedFailure(sqlite3.test.userfunctions.AuthorizerIllegalTypeTests('test_table_access')))
        #suite.addTest(unittest.expectedFailure(sqlite3.test.userfunctions.AuthorizerLargeIntegerTests('test_column_access')))
        #suite.addTest(unittest.expectedFailure(sqlite3.test.userfunctions.AuthorizerLargeIntegerTests('test_table_access')))
        #suite.addTest(unittest.expectedFailure(sqlite3.test.userfunctions.AuthorizerRaiseExceptionTests('test_column_access')))
        #suite.addTest(unittest.expectedFailure(sqlite3.test.userfunctions.AuthorizerRaiseExceptionTests('test_table_access')))
        #suite.addTest(unittest.expectedFailure(sqlite3.test.userfunctions.AuthorizerTests('test_column_access')))
        #suite.addTest(unittest.expectedFailure(sqlite3.test.userfunctions.AuthorizerTests('test_table_access')))
        suite.addTest(sqlite3.test.userfunctions.FunctionTests('CheckFuncErrorOnCreate'))
        suite.addTest(sqlite3.test.userfunctions.FunctionTests('CheckFuncException'))
        suite.addTest(sqlite3.test.userfunctions.FunctionTests('CheckFuncRefCount'))
        suite.addTest(unittest.expectedFailure(sqlite3.test.userfunctions.FunctionTests('CheckFuncReturnBlob')))
        suite.addTest(sqlite3.test.userfunctions.FunctionTests('CheckFuncReturnFloat'))
        suite.addTest(sqlite3.test.userfunctions.FunctionTests('CheckFuncReturnInt'))
        suite.addTest(sqlite3.test.userfunctions.FunctionTests('CheckFuncReturnLongLong'))
        suite.addTest(sqlite3.test.userfunctions.FunctionTests('CheckFuncReturnNull'))
        suite.addTest(sqlite3.test.userfunctions.FunctionTests('CheckFuncReturnText'))
        suite.addTest(sqlite3.test.userfunctions.FunctionTests('CheckFuncReturnUnicode'))
        suite.addTest(unittest.expectedFailure(sqlite3.test.userfunctions.FunctionTests('CheckParamBlob')))
        suite.addTest(sqlite3.test.userfunctions.FunctionTests('CheckParamFloat'))
        suite.addTest(sqlite3.test.userfunctions.FunctionTests('CheckParamInt'))
        suite.addTest(unittest.expectedFailure(sqlite3.test.userfunctions.FunctionTests('CheckParamLongLong')))
        suite.addTest(sqlite3.test.userfunctions.FunctionTests('CheckParamNone'))
        suite.addTest(sqlite3.test.userfunctions.FunctionTests('CheckParamString'))
        #suite.addTest(unittest.expectedFailure(sqlite3.test.userfunctions.AggregateTests('CheckAggrCheckAggrSum')))
        #suite.addTest(unittest.expectedFailure(sqlite3.test.userfunctions.AggregateTests('CheckAggrCheckParamBlob')))
        #suite.addTest(unittest.expectedFailure(sqlite3.test.userfunctions.AggregateTests('CheckAggrCheckParamFloat')))
        #suite.addTest(unittest.expectedFailure(sqlite3.test.userfunctions.AggregateTests('CheckAggrCheckParamInt')))
        #suite.addTest(unittest.expectedFailure(sqlite3.test.userfunctions.AggregateTests('CheckAggrCheckParamNone')))
        #suite.addTest(unittest.expectedFailure(sqlite3.test.userfunctions.AggregateTests('CheckAggrCheckParamStr')))
        #suite.addTest(unittest.expectedFailure(sqlite3.test.userfunctions.AggregateTests('CheckAggrErrorOnCreate')))
        #suite.addTest(unittest.expectedFailure(sqlite3.test.userfunctions.AggregateTests('CheckAggrExceptionInFinalize')))
        #suite.addTest(unittest.expectedFailure(sqlite3.test.userfunctions.AggregateTests('CheckAggrExceptionInInit')))
        #suite.addTest(unittest.expectedFailure(sqlite3.test.userfunctions.AggregateTests('CheckAggrExceptionInStep')))
        #suite.addTest(unittest.expectedFailure(sqlite3.test.userfunctions.AggregateTests('CheckAggrNoFinalize')))
        #suite.addTest(unittest.expectedFailure(sqlite3.test.userfunctions.AggregateTests('CheckAggrNoStep')))
        #suite.addTest(unittest.expectedFailure(sqlite3.test.userfunctions.AuthorizerTests('test_column_access')))
        #suite.addTest(unittest.expectedFailure(sqlite3.test.userfunctions.AuthorizerTests('test_table_access')))
        #suite.addTest(unittest.expectedFailure(sqlite3.test.userfunctions.AuthorizerRaiseExceptionTests('test_column_access')))
        #suite.addTest(unittest.expectedFailure(sqlite3.test.userfunctions.AuthorizerRaiseExceptionTests('test_table_access')))
        #suite.addTest(unittest.expectedFailure(sqlite3.test.userfunctions.AuthorizerIllegalTypeTests('test_column_access')))
        #suite.addTest(unittest.expectedFailure(sqlite3.test.userfunctions.AuthorizerIllegalTypeTests('test_table_access')))
        #suite.addTest(unittest.expectedFailure(sqlite3.test.userfunctions.AuthorizerLargeIntegerTests('test_column_access')))
        #suite.addTest(unittest.expectedFailure(sqlite3.test.userfunctions.AuthorizerLargeIntegerTests('test_table_access')))

        return suite

    else:
        return loader.loadTestsFromModule(sqlite3.test.dbapi, pattern)

run_test(__name__)
