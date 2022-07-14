// Licensed to the .NET Foundation under one or more agreements.
// The .NET Foundation licenses this file to you under the Apache 2.0 License.
// See the LICENSE file in the project root for more information.

using System;
using System.Runtime.CompilerServices;
using System.Runtime.InteropServices;

using IronPython.Runtime;

[assembly: PythonModule("errno", typeof(IronPython.Modules.PythonErrorNumber))]
namespace IronPython.Modules {
    public static class PythonErrorNumber {
        public const string __doc__ = "Provides a list of common error numbers.  These numbers are frequently reported in various exceptions.";

        internal const int ENOERROR = 0;

        #region Generated Errno Codes

        // *** BEGIN GENERATED CODE ***
        // generated by function: generate_errno_codes from: generate_errno.py


        public static int EPERM => 1;

        public static int ENOENT => 2;

        public static int ESRCH => 3;

        public static int EINTR => 4;

        public static int EIO => 5;

        public static int ENXIO => 6;

        public static int E2BIG => 7;

        public static int ENOEXEC => 8;

        public static int EBADF => 9;

        public static int ECHILD => 10;

        public static int EAGAIN => RuntimeInformation.IsOSPlatform(OSPlatform.Windows) ? 11 : RuntimeInformation.IsOSPlatform(OSPlatform.OSX) ? 35 : 11;

        public static int EWOULDBLOCK => RuntimeInformation.IsOSPlatform(OSPlatform.Windows) ? 10035 : RuntimeInformation.IsOSPlatform(OSPlatform.OSX) ? 35 : 11;

        public static int ENOMEM => 12;

        public static int EACCES => 13;

        public static int EFAULT => 14;

        [PythonHidden(PlatformsAttribute.PlatformFamily.Windows)]
        public static int ENOTBLK => 15;

        public static int EBUSY => 16;

        public static int EEXIST => 17;

        public static int EXDEV => 18;

        public static int ENODEV => 19;

        public static int ENOTDIR => 20;

        public static int EISDIR => 21;

        public static int EINVAL => 22;

        public static int ENFILE => 23;

        public static int EMFILE => 24;

        public static int ENOTTY => 25;

        public static int ETXTBSY => RuntimeInformation.IsOSPlatform(OSPlatform.Windows) ? 139 : 26;

        public static int EFBIG => 27;

        public static int ENOSPC => 28;

        public static int ESPIPE => 29;

        public static int EROFS => 30;

        public static int EMLINK => 31;

        public static int EPIPE => 32;

        public static int EDOM => 33;

        public static int ERANGE => 34;

        [PythonHidden(PlatformID.MacOSX)]
        public static int EDEADLOCK => RuntimeInformation.IsOSPlatform(OSPlatform.Windows) ? 36 : 35;

        public static int EDEADLK => RuntimeInformation.IsOSPlatform(OSPlatform.Windows) ? 36 : RuntimeInformation.IsOSPlatform(OSPlatform.OSX) ? 11 : 35;

        public static int ENAMETOOLONG => RuntimeInformation.IsOSPlatform(OSPlatform.Windows) ? 38 : RuntimeInformation.IsOSPlatform(OSPlatform.OSX) ? 63 : 36;

        public static int ENOLCK => RuntimeInformation.IsOSPlatform(OSPlatform.Windows) ? 39 : RuntimeInformation.IsOSPlatform(OSPlatform.OSX) ? 77 : 37;

        public static int ENOSYS => RuntimeInformation.IsOSPlatform(OSPlatform.Windows) ? 40 : RuntimeInformation.IsOSPlatform(OSPlatform.OSX) ? 78 : 38;

        public static int ENOTEMPTY => RuntimeInformation.IsOSPlatform(OSPlatform.Windows) ? 41 : RuntimeInformation.IsOSPlatform(OSPlatform.OSX) ? 66 : 39;

        public static int ELOOP => RuntimeInformation.IsOSPlatform(OSPlatform.Windows) ? 10062 : RuntimeInformation.IsOSPlatform(OSPlatform.OSX) ? 62 : 40;

        public static int ENOMSG => RuntimeInformation.IsOSPlatform(OSPlatform.Windows) ? 122 : RuntimeInformation.IsOSPlatform(OSPlatform.OSX) ? 91 : 42;

        public static int EIDRM => RuntimeInformation.IsOSPlatform(OSPlatform.Windows) ? 111 : RuntimeInformation.IsOSPlatform(OSPlatform.OSX) ? 90 : 43;

        [PythonHidden(PlatformsAttribute.PlatformFamily.Windows, PlatformID.MacOSX)]
        public static int ECHRNG => 44;

        [PythonHidden(PlatformsAttribute.PlatformFamily.Windows, PlatformID.MacOSX)]
        public static int EL2NSYNC => 45;

        [PythonHidden(PlatformsAttribute.PlatformFamily.Windows, PlatformID.MacOSX)]
        public static int EL3HLT => 46;

        [PythonHidden(PlatformsAttribute.PlatformFamily.Windows, PlatformID.MacOSX)]
        public static int EL3RST => 47;

        [PythonHidden(PlatformsAttribute.PlatformFamily.Windows, PlatformID.MacOSX)]
        public static int ELNRNG => 48;

        [PythonHidden(PlatformsAttribute.PlatformFamily.Windows, PlatformID.MacOSX)]
        public static int EUNATCH => 49;

        [PythonHidden(PlatformsAttribute.PlatformFamily.Windows, PlatformID.MacOSX)]
        public static int ENOCSI => 50;

        [PythonHidden(PlatformsAttribute.PlatformFamily.Windows, PlatformID.MacOSX)]
        public static int EL2HLT => 51;

        [PythonHidden(PlatformsAttribute.PlatformFamily.Windows, PlatformID.MacOSX)]
        public static int EBADE => 52;

        [PythonHidden(PlatformsAttribute.PlatformFamily.Windows, PlatformID.MacOSX)]
        public static int EBADR => 53;

        [PythonHidden(PlatformsAttribute.PlatformFamily.Windows, PlatformID.MacOSX)]
        public static int EXFULL => 54;

        [PythonHidden(PlatformsAttribute.PlatformFamily.Windows, PlatformID.MacOSX)]
        public static int ENOANO => 55;

        [PythonHidden(PlatformsAttribute.PlatformFamily.Windows, PlatformID.MacOSX)]
        public static int EBADRQC => 56;

        [PythonHidden(PlatformsAttribute.PlatformFamily.Windows, PlatformID.MacOSX)]
        public static int EBADSLT => 57;

        [PythonHidden(PlatformsAttribute.PlatformFamily.Windows, PlatformID.MacOSX)]
        public static int EBFONT => 59;

        public static int ENOSTR => RuntimeInformation.IsOSPlatform(OSPlatform.Windows) ? 125 : RuntimeInformation.IsOSPlatform(OSPlatform.OSX) ? 99 : 60;

        public static int ENODATA => RuntimeInformation.IsOSPlatform(OSPlatform.Windows) ? 120 : RuntimeInformation.IsOSPlatform(OSPlatform.OSX) ? 96 : 61;

        public static int ETIME => RuntimeInformation.IsOSPlatform(OSPlatform.Windows) ? 137 : RuntimeInformation.IsOSPlatform(OSPlatform.OSX) ? 101 : 62;

        public static int ENOSR => RuntimeInformation.IsOSPlatform(OSPlatform.Windows) ? 124 : RuntimeInformation.IsOSPlatform(OSPlatform.OSX) ? 98 : 63;

        [PythonHidden(PlatformsAttribute.PlatformFamily.Windows, PlatformID.MacOSX)]
        public static int ENONET => 64;

        [PythonHidden(PlatformsAttribute.PlatformFamily.Windows, PlatformID.MacOSX)]
        public static int ENOPKG => 65;

        public static int EREMOTE => RuntimeInformation.IsOSPlatform(OSPlatform.Windows) ? 10071 : RuntimeInformation.IsOSPlatform(OSPlatform.OSX) ? 71 : 66;

        public static int ENOLINK => RuntimeInformation.IsOSPlatform(OSPlatform.Windows) ? 121 : RuntimeInformation.IsOSPlatform(OSPlatform.OSX) ? 97 : 67;

        [PythonHidden(PlatformID.Unix)]
        public static int EPROCLIM => RuntimeInformation.IsOSPlatform(OSPlatform.Windows) ? 10067 : 67;

        [PythonHidden(PlatformsAttribute.PlatformFamily.Windows, PlatformID.MacOSX)]
        public static int EADV => 68;

        [PythonHidden(PlatformsAttribute.PlatformFamily.Windows, PlatformID.MacOSX)]
        public static int ESRMNT => 69;

        [PythonHidden(PlatformsAttribute.PlatformFamily.Windows, PlatformID.MacOSX)]
        public static int ECOMM => 70;

        public static int EPROTO => RuntimeInformation.IsOSPlatform(OSPlatform.Windows) ? 134 : RuntimeInformation.IsOSPlatform(OSPlatform.OSX) ? 100 : 71;

        [PythonHidden(PlatformsAttribute.PlatformFamily.Windows)]
        public static int EMULTIHOP => RuntimeInformation.IsOSPlatform(OSPlatform.OSX) ? 95 : 72;

        [PythonHidden(PlatformsAttribute.PlatformFamily.Windows, PlatformID.Unix)]
        public static int EBADRPC => 72;

        [PythonHidden(PlatformsAttribute.PlatformFamily.Windows, PlatformID.MacOSX)]
        public static int EDOTDOT => 73;

        [PythonHidden(PlatformsAttribute.PlatformFamily.Windows, PlatformID.Unix)]
        public static int ERPCMISMATCH => 73;

        public static int EBADMSG => RuntimeInformation.IsOSPlatform(OSPlatform.Windows) ? 104 : RuntimeInformation.IsOSPlatform(OSPlatform.OSX) ? 94 : 74;

        [PythonHidden(PlatformsAttribute.PlatformFamily.Windows, PlatformID.Unix)]
        public static int EPROGUNAVAIL => 74;

        public static int EOVERFLOW => RuntimeInformation.IsOSPlatform(OSPlatform.Windows) ? 132 : RuntimeInformation.IsOSPlatform(OSPlatform.OSX) ? 84 : 75;

        [PythonHidden(PlatformsAttribute.PlatformFamily.Windows, PlatformID.Unix)]
        public static int EPROGMISMATCH => 75;

        [PythonHidden(PlatformsAttribute.PlatformFamily.Windows, PlatformID.MacOSX)]
        public static int ENOTUNIQ => 76;

        [PythonHidden(PlatformsAttribute.PlatformFamily.Windows, PlatformID.Unix)]
        public static int EPROCUNAVAIL => 76;

        [PythonHidden(PlatformsAttribute.PlatformFamily.Windows, PlatformID.MacOSX)]
        public static int EBADFD => 77;

        [PythonHidden(PlatformsAttribute.PlatformFamily.Windows, PlatformID.MacOSX)]
        public static int EREMCHG => 78;

        [PythonHidden(PlatformsAttribute.PlatformFamily.Windows, PlatformID.MacOSX)]
        public static int ELIBACC => 79;

        [PythonHidden(PlatformsAttribute.PlatformFamily.Windows, PlatformID.Unix)]
        public static int EFTYPE => 79;

        [PythonHidden(PlatformsAttribute.PlatformFamily.Windows, PlatformID.MacOSX)]
        public static int ELIBBAD => 80;

        [PythonHidden(PlatformsAttribute.PlatformFamily.Windows, PlatformID.Unix)]
        public static int EAUTH => 80;

        [PythonHidden(PlatformsAttribute.PlatformFamily.Windows, PlatformID.MacOSX)]
        public static int ELIBSCN => 81;

        [PythonHidden(PlatformsAttribute.PlatformFamily.Windows, PlatformID.Unix)]
        public static int ENEEDAUTH => 81;

        [PythonHidden(PlatformsAttribute.PlatformFamily.Windows, PlatformID.MacOSX)]
        public static int ELIBMAX => 82;

        [PythonHidden(PlatformsAttribute.PlatformFamily.Windows, PlatformID.Unix)]
        public static int EPWROFF => 82;

        [PythonHidden(PlatformsAttribute.PlatformFamily.Windows, PlatformID.MacOSX)]
        public static int ELIBEXEC => 83;

        [PythonHidden(PlatformsAttribute.PlatformFamily.Windows, PlatformID.Unix)]
        public static int EDEVERR => 83;

        public static int EILSEQ => RuntimeInformation.IsOSPlatform(OSPlatform.Windows) ? 42 : RuntimeInformation.IsOSPlatform(OSPlatform.OSX) ? 92 : 84;

        [PythonHidden(PlatformsAttribute.PlatformFamily.Windows, PlatformID.MacOSX)]
        public static int ERESTART => 85;

        [PythonHidden(PlatformsAttribute.PlatformFamily.Windows, PlatformID.Unix)]
        public static int EBADEXEC => 85;

        [PythonHidden(PlatformsAttribute.PlatformFamily.Windows, PlatformID.MacOSX)]
        public static int ESTRPIPE => 86;

        [PythonHidden(PlatformsAttribute.PlatformFamily.Windows, PlatformID.Unix)]
        public static int EBADARCH => 86;

        public static int EUSERS => RuntimeInformation.IsOSPlatform(OSPlatform.Windows) ? 10068 : RuntimeInformation.IsOSPlatform(OSPlatform.OSX) ? 68 : 87;

        [PythonHidden(PlatformsAttribute.PlatformFamily.Windows, PlatformID.Unix)]
        public static int ESHLIBVERS => 87;

        public static int ENOTSOCK => RuntimeInformation.IsOSPlatform(OSPlatform.Windows) ? 10038 : RuntimeInformation.IsOSPlatform(OSPlatform.OSX) ? 38 : 88;

        [PythonHidden(PlatformsAttribute.PlatformFamily.Windows, PlatformID.Unix)]
        public static int EBADMACHO => 88;

        public static int EDESTADDRREQ => RuntimeInformation.IsOSPlatform(OSPlatform.Windows) ? 10039 : RuntimeInformation.IsOSPlatform(OSPlatform.OSX) ? 39 : 89;

        public static int EMSGSIZE => RuntimeInformation.IsOSPlatform(OSPlatform.Windows) ? 10040 : RuntimeInformation.IsOSPlatform(OSPlatform.OSX) ? 40 : 90;

        public static int EPROTOTYPE => RuntimeInformation.IsOSPlatform(OSPlatform.Windows) ? 10041 : RuntimeInformation.IsOSPlatform(OSPlatform.OSX) ? 41 : 91;

        public static int ENOPROTOOPT => RuntimeInformation.IsOSPlatform(OSPlatform.Windows) ? 10042 : RuntimeInformation.IsOSPlatform(OSPlatform.OSX) ? 42 : 92;

        public static int EPROTONOSUPPORT => RuntimeInformation.IsOSPlatform(OSPlatform.Windows) ? 10043 : RuntimeInformation.IsOSPlatform(OSPlatform.OSX) ? 43 : 93;

        [PythonHidden(PlatformsAttribute.PlatformFamily.Windows, PlatformID.Unix)]
        public static int ENOATTR => 93;

        public static int ESOCKTNOSUPPORT => RuntimeInformation.IsOSPlatform(OSPlatform.Windows) ? 10044 : RuntimeInformation.IsOSPlatform(OSPlatform.OSX) ? 44 : 94;

        public static int ENOTSUP => RuntimeInformation.IsOSPlatform(OSPlatform.Windows) ? 129 : RuntimeInformation.IsOSPlatform(OSPlatform.OSX) ? 45 : 95;

        public static int EOPNOTSUPP => RuntimeInformation.IsOSPlatform(OSPlatform.Windows) ? 10045 : RuntimeInformation.IsOSPlatform(OSPlatform.OSX) ? 102 : 95;

        public static int EPFNOSUPPORT => RuntimeInformation.IsOSPlatform(OSPlatform.Windows) ? 10046 : RuntimeInformation.IsOSPlatform(OSPlatform.OSX) ? 46 : 96;

        public static int EAFNOSUPPORT => RuntimeInformation.IsOSPlatform(OSPlatform.Windows) ? 10047 : RuntimeInformation.IsOSPlatform(OSPlatform.OSX) ? 47 : 97;

        public static int EADDRINUSE => RuntimeInformation.IsOSPlatform(OSPlatform.Windows) ? 10048 : RuntimeInformation.IsOSPlatform(OSPlatform.OSX) ? 48 : 98;

        public static int EADDRNOTAVAIL => RuntimeInformation.IsOSPlatform(OSPlatform.Windows) ? 10049 : RuntimeInformation.IsOSPlatform(OSPlatform.OSX) ? 49 : 99;

        public static int ENETDOWN => RuntimeInformation.IsOSPlatform(OSPlatform.Windows) ? 10050 : RuntimeInformation.IsOSPlatform(OSPlatform.OSX) ? 50 : 100;

        public static int ENETUNREACH => RuntimeInformation.IsOSPlatform(OSPlatform.Windows) ? 10051 : RuntimeInformation.IsOSPlatform(OSPlatform.OSX) ? 51 : 101;

        public static int ENETRESET => RuntimeInformation.IsOSPlatform(OSPlatform.Windows) ? 10052 : RuntimeInformation.IsOSPlatform(OSPlatform.OSX) ? 52 : 102;

        public static int ECONNABORTED => RuntimeInformation.IsOSPlatform(OSPlatform.Windows) ? 10053 : RuntimeInformation.IsOSPlatform(OSPlatform.OSX) ? 53 : 103;

        [PythonHidden(PlatformsAttribute.PlatformFamily.Windows, PlatformID.Unix)]
        public static int ENOPOLICY => 103;

        public static int ECONNRESET => RuntimeInformation.IsOSPlatform(OSPlatform.Windows) ? 10054 : RuntimeInformation.IsOSPlatform(OSPlatform.OSX) ? 54 : 104;

        public static int ENOBUFS => RuntimeInformation.IsOSPlatform(OSPlatform.Windows) ? 10055 : RuntimeInformation.IsOSPlatform(OSPlatform.OSX) ? 55 : 105;

        public static int EISCONN => RuntimeInformation.IsOSPlatform(OSPlatform.Windows) ? 10056 : RuntimeInformation.IsOSPlatform(OSPlatform.OSX) ? 56 : 106;

        public static int ENOTCONN => RuntimeInformation.IsOSPlatform(OSPlatform.Windows) ? 10057 : RuntimeInformation.IsOSPlatform(OSPlatform.OSX) ? 57 : 107;

        public static int ESHUTDOWN => RuntimeInformation.IsOSPlatform(OSPlatform.Windows) ? 10058 : RuntimeInformation.IsOSPlatform(OSPlatform.OSX) ? 58 : 108;

        public static int ETOOMANYREFS => RuntimeInformation.IsOSPlatform(OSPlatform.Windows) ? 10059 : RuntimeInformation.IsOSPlatform(OSPlatform.OSX) ? 59 : 109;

        public static int ETIMEDOUT => RuntimeInformation.IsOSPlatform(OSPlatform.Windows) ? 10060 : RuntimeInformation.IsOSPlatform(OSPlatform.OSX) ? 60 : 110;

        public static int ECONNREFUSED => RuntimeInformation.IsOSPlatform(OSPlatform.Windows) ? 10061 : RuntimeInformation.IsOSPlatform(OSPlatform.OSX) ? 61 : 111;

        public static int EHOSTDOWN => RuntimeInformation.IsOSPlatform(OSPlatform.Windows) ? 10064 : RuntimeInformation.IsOSPlatform(OSPlatform.OSX) ? 64 : 112;

        public static int EHOSTUNREACH => RuntimeInformation.IsOSPlatform(OSPlatform.Windows) ? 10065 : RuntimeInformation.IsOSPlatform(OSPlatform.OSX) ? 65 : 113;

        public static int EALREADY => RuntimeInformation.IsOSPlatform(OSPlatform.Windows) ? 10037 : RuntimeInformation.IsOSPlatform(OSPlatform.OSX) ? 37 : 114;

        public static int EINPROGRESS => RuntimeInformation.IsOSPlatform(OSPlatform.Windows) ? 10036 : RuntimeInformation.IsOSPlatform(OSPlatform.OSX) ? 36 : 115;

        public static int ESTALE => RuntimeInformation.IsOSPlatform(OSPlatform.Windows) ? 10070 : RuntimeInformation.IsOSPlatform(OSPlatform.OSX) ? 70 : 116;

        [PythonHidden(PlatformsAttribute.PlatformFamily.Windows, PlatformID.MacOSX)]
        public static int EUCLEAN => 117;

        [PythonHidden(PlatformsAttribute.PlatformFamily.Windows, PlatformID.MacOSX)]
        public static int ENOTNAM => 118;

        [PythonHidden(PlatformsAttribute.PlatformFamily.Windows, PlatformID.MacOSX)]
        public static int ENAVAIL => 119;

        [PythonHidden(PlatformsAttribute.PlatformFamily.Windows, PlatformID.MacOSX)]
        public static int EISNAM => 120;

        [PythonHidden(PlatformsAttribute.PlatformFamily.Windows, PlatformID.MacOSX)]
        public static int EREMOTEIO => 121;

        public static int EDQUOT => RuntimeInformation.IsOSPlatform(OSPlatform.Windows) ? 10069 : RuntimeInformation.IsOSPlatform(OSPlatform.OSX) ? 69 : 122;

        [PythonHidden(PlatformsAttribute.PlatformFamily.Windows, PlatformID.MacOSX)]
        public static int ENOMEDIUM => 123;

        [PythonHidden(PlatformsAttribute.PlatformFamily.Windows, PlatformID.MacOSX)]
        public static int EMEDIUMTYPE => 124;

        public static int ECANCELED => RuntimeInformation.IsOSPlatform(OSPlatform.Windows) ? 105 : RuntimeInformation.IsOSPlatform(OSPlatform.OSX) ? 89 : 125;

        [PythonHidden(PlatformsAttribute.PlatformFamily.Windows, PlatformID.MacOSX)]
        public static int ENOKEY => 126;

        [PythonHidden(PlatformsAttribute.PlatformFamily.Windows, PlatformID.MacOSX)]
        public static int EKEYEXPIRED => 127;

        [PythonHidden(PlatformsAttribute.PlatformFamily.Windows, PlatformID.MacOSX)]
        public static int EKEYREVOKED => 128;

        [PythonHidden(PlatformsAttribute.PlatformFamily.Windows, PlatformID.MacOSX)]
        public static int EKEYREJECTED => 129;

        public static int EOWNERDEAD => RuntimeInformation.IsOSPlatform(OSPlatform.Windows) ? 133 : RuntimeInformation.IsOSPlatform(OSPlatform.OSX) ? 105 : 130;

        public static int ENOTRECOVERABLE => RuntimeInformation.IsOSPlatform(OSPlatform.Windows) ? 127 : RuntimeInformation.IsOSPlatform(OSPlatform.OSX) ? 104 : 131;

        [PythonHidden(PlatformsAttribute.PlatformFamily.Windows, PlatformID.MacOSX)]
        public static int ERFKILL => 132;

        [PythonHidden(PlatformsAttribute.PlatformFamily.Unix)]
        public static int WSABASEERR => 10000;

        [PythonHidden(PlatformsAttribute.PlatformFamily.Unix)]
        public static int WSAEINTR => 10004;

        [PythonHidden(PlatformsAttribute.PlatformFamily.Unix)]
        public static int WSAEBADF => 10009;

        [PythonHidden(PlatformsAttribute.PlatformFamily.Unix)]
        public static int WSAEACCES => 10013;

        [PythonHidden(PlatformsAttribute.PlatformFamily.Unix)]
        public static int WSAEFAULT => 10014;

        [PythonHidden(PlatformsAttribute.PlatformFamily.Unix)]
        public static int WSAEINVAL => 10022;

        [PythonHidden(PlatformsAttribute.PlatformFamily.Unix)]
        public static int WSAEMFILE => 10024;

        [PythonHidden(PlatformsAttribute.PlatformFamily.Unix)]
        public static int WSAEWOULDBLOCK => 10035;

        [PythonHidden(PlatformsAttribute.PlatformFamily.Unix)]
        public static int WSAEINPROGRESS => 10036;

        [PythonHidden(PlatformsAttribute.PlatformFamily.Unix)]
        public static int WSAEALREADY => 10037;

        [PythonHidden(PlatformsAttribute.PlatformFamily.Unix)]
        public static int WSAENOTSOCK => 10038;

        [PythonHidden(PlatformsAttribute.PlatformFamily.Unix)]
        public static int WSAEDESTADDRREQ => 10039;

        [PythonHidden(PlatformsAttribute.PlatformFamily.Unix)]
        public static int WSAEMSGSIZE => 10040;

        [PythonHidden(PlatformsAttribute.PlatformFamily.Unix)]
        public static int WSAEPROTOTYPE => 10041;

        [PythonHidden(PlatformsAttribute.PlatformFamily.Unix)]
        public static int WSAENOPROTOOPT => 10042;

        [PythonHidden(PlatformsAttribute.PlatformFamily.Unix)]
        public static int WSAEPROTONOSUPPORT => 10043;

        [PythonHidden(PlatformsAttribute.PlatformFamily.Unix)]
        public static int WSAESOCKTNOSUPPORT => 10044;

        [PythonHidden(PlatformsAttribute.PlatformFamily.Unix)]
        public static int WSAEOPNOTSUPP => 10045;

        [PythonHidden(PlatformsAttribute.PlatformFamily.Unix)]
        public static int WSAEPFNOSUPPORT => 10046;

        [PythonHidden(PlatformsAttribute.PlatformFamily.Unix)]
        public static int WSAEAFNOSUPPORT => 10047;

        [PythonHidden(PlatformsAttribute.PlatformFamily.Unix)]
        public static int WSAEADDRINUSE => 10048;

        [PythonHidden(PlatformsAttribute.PlatformFamily.Unix)]
        public static int WSAEADDRNOTAVAIL => 10049;

        [PythonHidden(PlatformsAttribute.PlatformFamily.Unix)]
        public static int WSAENETDOWN => 10050;

        [PythonHidden(PlatformsAttribute.PlatformFamily.Unix)]
        public static int WSAENETUNREACH => 10051;

        [PythonHidden(PlatformsAttribute.PlatformFamily.Unix)]
        public static int WSAENETRESET => 10052;

        [PythonHidden(PlatformsAttribute.PlatformFamily.Unix)]
        public static int WSAECONNABORTED => 10053;

        [PythonHidden(PlatformsAttribute.PlatformFamily.Unix)]
        public static int WSAECONNRESET => 10054;

        [PythonHidden(PlatformsAttribute.PlatformFamily.Unix)]
        public static int WSAENOBUFS => 10055;

        [PythonHidden(PlatformsAttribute.PlatformFamily.Unix)]
        public static int WSAEISCONN => 10056;

        [PythonHidden(PlatformsAttribute.PlatformFamily.Unix)]
        public static int WSAENOTCONN => 10057;

        [PythonHidden(PlatformsAttribute.PlatformFamily.Unix)]
        public static int WSAESHUTDOWN => 10058;

        [PythonHidden(PlatformsAttribute.PlatformFamily.Unix)]
        public static int WSAETOOMANYREFS => 10059;

        [PythonHidden(PlatformsAttribute.PlatformFamily.Unix)]
        public static int WSAETIMEDOUT => 10060;

        [PythonHidden(PlatformsAttribute.PlatformFamily.Unix)]
        public static int WSAECONNREFUSED => 10061;

        [PythonHidden(PlatformsAttribute.PlatformFamily.Unix)]
        public static int WSAELOOP => 10062;

        [PythonHidden(PlatformsAttribute.PlatformFamily.Unix)]
        public static int WSAENAMETOOLONG => 10063;

        [PythonHidden(PlatformsAttribute.PlatformFamily.Unix)]
        public static int WSAEHOSTDOWN => 10064;

        [PythonHidden(PlatformsAttribute.PlatformFamily.Unix)]
        public static int WSAEHOSTUNREACH => 10065;

        [PythonHidden(PlatformsAttribute.PlatformFamily.Unix)]
        public static int WSAENOTEMPTY => 10066;

        [PythonHidden(PlatformsAttribute.PlatformFamily.Unix)]
        public static int WSAEPROCLIM => 10067;

        [PythonHidden(PlatformsAttribute.PlatformFamily.Unix)]
        public static int WSAEUSERS => 10068;

        [PythonHidden(PlatformsAttribute.PlatformFamily.Unix)]
        public static int WSAEDQUOT => 10069;

        [PythonHidden(PlatformsAttribute.PlatformFamily.Unix)]
        public static int WSAESTALE => 10070;

        [PythonHidden(PlatformsAttribute.PlatformFamily.Unix)]
        public static int WSAEREMOTE => 10071;

        [PythonHidden(PlatformsAttribute.PlatformFamily.Unix)]
        public static int WSASYSNOTREADY => 10091;

        [PythonHidden(PlatformsAttribute.PlatformFamily.Unix)]
        public static int WSAVERNOTSUPPORTED => 10092;

        [PythonHidden(PlatformsAttribute.PlatformFamily.Unix)]
        public static int WSANOTINITIALISED => 10093;

        [PythonHidden(PlatformsAttribute.PlatformFamily.Unix)]
        public static int WSAEDISCON => 10101;

        // *** END GENERATED CODE ***

        #endregion

        [SpecialName]
        public static void PerformModuleReload(PythonContext/*!*/ context, PythonDictionary/*!*/ dict) {
            PythonDictionary errorcode = new PythonDictionary();

            #region Generated Errno Names

            // *** BEGIN GENERATED CODE ***
            // generated by function: generate_errno_names from: generate_errno.py

            // names defined on all platforms
            errorcode[E2BIG] = "E2BIG";
            errorcode[EACCES] = "EACCES";
            errorcode[EAGAIN] = "EAGAIN";
            errorcode[EBADF] = "EBADF";
            errorcode[EBADMSG] = "EBADMSG";
            errorcode[EBUSY] = "EBUSY";
            errorcode[ECANCELED] = "ECANCELED";
            errorcode[ECHILD] = "ECHILD";
            errorcode[EDOM] = "EDOM";
            errorcode[EEXIST] = "EEXIST";
            errorcode[EFAULT] = "EFAULT";
            errorcode[EFBIG] = "EFBIG";
            errorcode[EIDRM] = "EIDRM";
            errorcode[EILSEQ] = "EILSEQ";
            errorcode[EINTR] = "EINTR";
            errorcode[EINVAL] = "EINVAL";
            errorcode[EIO] = "EIO";
            errorcode[EISDIR] = "EISDIR";
            errorcode[EMFILE] = "EMFILE";
            errorcode[EMLINK] = "EMLINK";
            errorcode[ENAMETOOLONG] = "ENAMETOOLONG";
            errorcode[ENFILE] = "ENFILE";
            errorcode[ENODATA] = "ENODATA";
            errorcode[ENODEV] = "ENODEV";
            errorcode[ENOENT] = "ENOENT";
            errorcode[ENOEXEC] = "ENOEXEC";
            errorcode[ENOLCK] = "ENOLCK";
            errorcode[ENOLINK] = "ENOLINK";
            errorcode[ENOMEM] = "ENOMEM";
            errorcode[ENOMSG] = "ENOMSG";
            errorcode[ENOSPC] = "ENOSPC";
            errorcode[ENOSR] = "ENOSR";
            errorcode[ENOSTR] = "ENOSTR";
            errorcode[ENOSYS] = "ENOSYS";
            errorcode[ENOTDIR] = "ENOTDIR";
            errorcode[ENOTEMPTY] = "ENOTEMPTY";
            errorcode[ENOTRECOVERABLE] = "ENOTRECOVERABLE";
            errorcode[ENOTSUP] = "ENOTSUP";
            errorcode[ENOTTY] = "ENOTTY";
            errorcode[ENXIO] = "ENXIO";
            errorcode[EOVERFLOW] = "EOVERFLOW";
            errorcode[EOWNERDEAD] = "EOWNERDEAD";
            errorcode[EPERM] = "EPERM";
            errorcode[EPIPE] = "EPIPE";
            errorcode[EPROTO] = "EPROTO";
            errorcode[ERANGE] = "ERANGE";
            errorcode[EROFS] = "EROFS";
            errorcode[ESPIPE] = "ESPIPE";
            errorcode[ESRCH] = "ESRCH";
            errorcode[ETIME] = "ETIME";
            errorcode[ETXTBSY] = "ETXTBSY";
            errorcode[EXDEV] = "EXDEV";
            // names defined on Posix platforms
            if (RuntimeInformation.IsOSPlatform(OSPlatform.Linux) || RuntimeInformation.IsOSPlatform(OSPlatform.OSX)) {
                errorcode[EADDRINUSE] = "EADDRINUSE";
                errorcode[EADDRNOTAVAIL] = "EADDRNOTAVAIL";
                errorcode[EAFNOSUPPORT] = "EAFNOSUPPORT";
                errorcode[EALREADY] = "EALREADY";
                errorcode[ECONNABORTED] = "ECONNABORTED";
                errorcode[ECONNREFUSED] = "ECONNREFUSED";
                errorcode[ECONNRESET] = "ECONNRESET";
                errorcode[EDESTADDRREQ] = "EDESTADDRREQ";
                errorcode[EDQUOT] = "EDQUOT";
                errorcode[EHOSTDOWN] = "EHOSTDOWN";
                errorcode[EHOSTUNREACH] = "EHOSTUNREACH";
                errorcode[EINPROGRESS] = "EINPROGRESS";
                errorcode[EISCONN] = "EISCONN";
                errorcode[ELOOP] = "ELOOP";
                errorcode[EMSGSIZE] = "EMSGSIZE";
                errorcode[EMULTIHOP] = "EMULTIHOP";
                errorcode[ENETDOWN] = "ENETDOWN";
                errorcode[ENETRESET] = "ENETRESET";
                errorcode[ENETUNREACH] = "ENETUNREACH";
                errorcode[ENOBUFS] = "ENOBUFS";
                errorcode[ENOPROTOOPT] = "ENOPROTOOPT";
                errorcode[ENOTBLK] = "ENOTBLK";
                errorcode[ENOTCONN] = "ENOTCONN";
                errorcode[ENOTSOCK] = "ENOTSOCK";
                errorcode[EPFNOSUPPORT] = "EPFNOSUPPORT";
                errorcode[EPROTONOSUPPORT] = "EPROTONOSUPPORT";
                errorcode[EPROTOTYPE] = "EPROTOTYPE";
                errorcode[EREMOTE] = "EREMOTE";
                errorcode[ESHUTDOWN] = "ESHUTDOWN";
                errorcode[ESOCKTNOSUPPORT] = "ESOCKTNOSUPPORT";
                errorcode[ESTALE] = "ESTALE";
                errorcode[ETIMEDOUT] = "ETIMEDOUT";
                errorcode[ETOOMANYREFS] = "ETOOMANYREFS";
                errorcode[EUSERS] = "EUSERS";
            }
            // names defined on Linux
            if (RuntimeInformation.IsOSPlatform(OSPlatform.Linux)) {
                errorcode[EADV] = "EADV";
                errorcode[EBADE] = "EBADE";
                errorcode[EBADFD] = "EBADFD";
                errorcode[EBADR] = "EBADR";
                errorcode[EBADRQC] = "EBADRQC";
                errorcode[EBADSLT] = "EBADSLT";
                errorcode[EBFONT] = "EBFONT";
                errorcode[ECHRNG] = "ECHRNG";
                errorcode[ECOMM] = "ECOMM";
                errorcode[EDEADLOCK] = "EDEADLOCK";
                errorcode[EDOTDOT] = "EDOTDOT";
                errorcode[EISNAM] = "EISNAM";
                errorcode[EKEYEXPIRED] = "EKEYEXPIRED";
                errorcode[EKEYREJECTED] = "EKEYREJECTED";
                errorcode[EKEYREVOKED] = "EKEYREVOKED";
                errorcode[EL2HLT] = "EL2HLT";
                errorcode[EL2NSYNC] = "EL2NSYNC";
                errorcode[EL3HLT] = "EL3HLT";
                errorcode[EL3RST] = "EL3RST";
                errorcode[ELIBACC] = "ELIBACC";
                errorcode[ELIBBAD] = "ELIBBAD";
                errorcode[ELIBEXEC] = "ELIBEXEC";
                errorcode[ELIBMAX] = "ELIBMAX";
                errorcode[ELIBSCN] = "ELIBSCN";
                errorcode[ELNRNG] = "ELNRNG";
                errorcode[EMEDIUMTYPE] = "EMEDIUMTYPE";
                errorcode[ENAVAIL] = "ENAVAIL";
                errorcode[ENOANO] = "ENOANO";
                errorcode[ENOCSI] = "ENOCSI";
                errorcode[ENOKEY] = "ENOKEY";
                errorcode[ENOMEDIUM] = "ENOMEDIUM";
                errorcode[ENONET] = "ENONET";
                errorcode[ENOPKG] = "ENOPKG";
                errorcode[ENOTNAM] = "ENOTNAM";
                errorcode[ENOTUNIQ] = "ENOTUNIQ";
                errorcode[EREMCHG] = "EREMCHG";
                errorcode[EREMOTEIO] = "EREMOTEIO";
                errorcode[ERESTART] = "ERESTART";
                errorcode[ERFKILL] = "ERFKILL";
                errorcode[ESRMNT] = "ESRMNT";
                errorcode[ESTRPIPE] = "ESTRPIPE";
                errorcode[EUCLEAN] = "EUCLEAN";
                errorcode[EUNATCH] = "EUNATCH";
                errorcode[EXFULL] = "EXFULL";
            }
            // names defined on macOS
            if (RuntimeInformation.IsOSPlatform(OSPlatform.OSX)) {
                errorcode[EAUTH] = "EAUTH";
                errorcode[EBADARCH] = "EBADARCH";
                errorcode[EBADEXEC] = "EBADEXEC";
                errorcode[EBADMACHO] = "EBADMACHO";
                errorcode[EBADRPC] = "EBADRPC";
                errorcode[EDEADLK] = "EDEADLK";
                errorcode[EDEVERR] = "EDEVERR";
                errorcode[EFTYPE] = "EFTYPE";
                errorcode[ENEEDAUTH] = "ENEEDAUTH";
                errorcode[ENOATTR] = "ENOATTR";
                errorcode[ENOPOLICY] = "ENOPOLICY";
                errorcode[EOPNOTSUPP] = "EOPNOTSUPP";
                errorcode[EPROCLIM] = "EPROCLIM";
                errorcode[EPROCUNAVAIL] = "EPROCUNAVAIL";
                errorcode[EPROGMISMATCH] = "EPROGMISMATCH";
                errorcode[EPROGUNAVAIL] = "EPROGUNAVAIL";
                errorcode[EPWROFF] = "EPWROFF";
                errorcode[ERPCMISMATCH] = "ERPCMISMATCH";
                errorcode[ESHLIBVERS] = "ESHLIBVERS";
            }
            // names defined on Windows
            if (RuntimeInformation.IsOSPlatform(OSPlatform.Windows)) {
                errorcode[EADDRINUSE] = "EADDRINUSE";
                errorcode[EADDRNOTAVAIL] = "EADDRNOTAVAIL";
                errorcode[EAFNOSUPPORT] = "EAFNOSUPPORT";
                errorcode[EALREADY] = "EALREADY";
                errorcode[ECONNABORTED] = "ECONNABORTED";
                errorcode[ECONNREFUSED] = "ECONNREFUSED";
                errorcode[ECONNRESET] = "ECONNRESET";
                errorcode[EDEADLK] = "EDEADLK";
                errorcode[EDEADLOCK] = "EDEADLOCK";
                errorcode[EDESTADDRREQ] = "EDESTADDRREQ";
                errorcode[EDQUOT] = "EDQUOT";
                errorcode[EHOSTDOWN] = "EHOSTDOWN";
                errorcode[EHOSTUNREACH] = "EHOSTUNREACH";
                errorcode[EINPROGRESS] = "EINPROGRESS";
                errorcode[EISCONN] = "EISCONN";
                errorcode[ELOOP] = "ELOOP";
                errorcode[EMSGSIZE] = "EMSGSIZE";
                errorcode[ENETDOWN] = "ENETDOWN";
                errorcode[ENETRESET] = "ENETRESET";
                errorcode[ENETUNREACH] = "ENETUNREACH";
                errorcode[ENOBUFS] = "ENOBUFS";
                errorcode[ENOPROTOOPT] = "ENOPROTOOPT";
                errorcode[ENOTCONN] = "ENOTCONN";
                errorcode[ENOTSOCK] = "ENOTSOCK";
                errorcode[EOPNOTSUPP] = "EOPNOTSUPP";
                errorcode[EPFNOSUPPORT] = "EPFNOSUPPORT";
                errorcode[EPROCLIM] = "EPROCLIM";
                errorcode[EPROTONOSUPPORT] = "EPROTONOSUPPORT";
                errorcode[EPROTOTYPE] = "EPROTOTYPE";
                errorcode[EREMOTE] = "EREMOTE";
                errorcode[ESHUTDOWN] = "ESHUTDOWN";
                errorcode[ESOCKTNOSUPPORT] = "ESOCKTNOSUPPORT";
                errorcode[ESTALE] = "ESTALE";
                errorcode[ETIMEDOUT] = "ETIMEDOUT";
                errorcode[ETOOMANYREFS] = "ETOOMANYREFS";
                errorcode[EUSERS] = "EUSERS";
                errorcode[EWOULDBLOCK] = "EWOULDBLOCK";
                errorcode[WSABASEERR] = "WSABASEERR";
                errorcode[WSAEACCES] = "WSAEACCES";
                errorcode[WSAEADDRINUSE] = "WSAEADDRINUSE";
                errorcode[WSAEADDRNOTAVAIL] = "WSAEADDRNOTAVAIL";
                errorcode[WSAEAFNOSUPPORT] = "WSAEAFNOSUPPORT";
                errorcode[WSAEALREADY] = "WSAEALREADY";
                errorcode[WSAEBADF] = "WSAEBADF";
                errorcode[WSAECONNABORTED] = "WSAECONNABORTED";
                errorcode[WSAECONNREFUSED] = "WSAECONNREFUSED";
                errorcode[WSAECONNRESET] = "WSAECONNRESET";
                errorcode[WSAEDESTADDRREQ] = "WSAEDESTADDRREQ";
                errorcode[WSAEDISCON] = "WSAEDISCON";
                errorcode[WSAEDQUOT] = "WSAEDQUOT";
                errorcode[WSAEFAULT] = "WSAEFAULT";
                errorcode[WSAEHOSTDOWN] = "WSAEHOSTDOWN";
                errorcode[WSAEHOSTUNREACH] = "WSAEHOSTUNREACH";
                errorcode[WSAEINPROGRESS] = "WSAEINPROGRESS";
                errorcode[WSAEINTR] = "WSAEINTR";
                errorcode[WSAEINVAL] = "WSAEINVAL";
                errorcode[WSAEISCONN] = "WSAEISCONN";
                errorcode[WSAELOOP] = "WSAELOOP";
                errorcode[WSAEMFILE] = "WSAEMFILE";
                errorcode[WSAEMSGSIZE] = "WSAEMSGSIZE";
                errorcode[WSAENAMETOOLONG] = "WSAENAMETOOLONG";
                errorcode[WSAENETDOWN] = "WSAENETDOWN";
                errorcode[WSAENETRESET] = "WSAENETRESET";
                errorcode[WSAENETUNREACH] = "WSAENETUNREACH";
                errorcode[WSAENOBUFS] = "WSAENOBUFS";
                errorcode[WSAENOPROTOOPT] = "WSAENOPROTOOPT";
                errorcode[WSAENOTCONN] = "WSAENOTCONN";
                errorcode[WSAENOTEMPTY] = "WSAENOTEMPTY";
                errorcode[WSAENOTSOCK] = "WSAENOTSOCK";
                errorcode[WSAEOPNOTSUPP] = "WSAEOPNOTSUPP";
                errorcode[WSAEPFNOSUPPORT] = "WSAEPFNOSUPPORT";
                errorcode[WSAEPROCLIM] = "WSAEPROCLIM";
                errorcode[WSAEPROTONOSUPPORT] = "WSAEPROTONOSUPPORT";
                errorcode[WSAEPROTOTYPE] = "WSAEPROTOTYPE";
                errorcode[WSAEREMOTE] = "WSAEREMOTE";
                errorcode[WSAESHUTDOWN] = "WSAESHUTDOWN";
                errorcode[WSAESOCKTNOSUPPORT] = "WSAESOCKTNOSUPPORT";
                errorcode[WSAESTALE] = "WSAESTALE";
                errorcode[WSAETIMEDOUT] = "WSAETIMEDOUT";
                errorcode[WSAETOOMANYREFS] = "WSAETOOMANYREFS";
                errorcode[WSAEUSERS] = "WSAEUSERS";
                errorcode[WSAEWOULDBLOCK] = "WSAEWOULDBLOCK";
                errorcode[WSANOTINITIALISED] = "WSANOTINITIALISED";
                errorcode[WSASYSNOTREADY] = "WSASYSNOTREADY";
                errorcode[WSAVERNOTSUPPORTED] = "WSAVERNOTSUPPORTED";
            }

            // *** END GENERATED CODE ***

            #endregion

            dict["errorcode"] = errorcode;
        }
    }
}
