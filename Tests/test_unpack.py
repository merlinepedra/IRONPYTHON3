# Licensed to the .NET Foundation under one or more agreements.
# The .NET Foundation licenses this file to you under the Apache 2.0 License.
# See the LICENSE file in the project root for more information.

import sys
import test.support
import unittest

class UnpackTest(unittest.TestCase):
    def assertRaisesSyntaxError(self, body, expectedMessage, lineno = 1):
        with self.assertRaises(SyntaxError) as context:
            exec(body)
        self.assertEqual(context.exception.msg, expectedMessage, "Error raised, but wrong message")
        self.assertEqual(context.exception.lineno, lineno, "Error raised, but on the wrong line")

    def test_unpack_into_exprlist_1(self):
        *a, = range(2)
        self.assertEqual(a, [0, 1])

    def test_unpack_into_exprlist_2(self):
        *a, b, c = range(6)
        self.assertEqual(a, [0, 1, 2, 3])
        self.assertEqual(b, 4)
        self.assertEqual(c, 5)

    def test_unpack_into_exprlist_3(self):
        a, *b, c = range(6)
        self.assertEqual(a, 0)
        self.assertEqual(b, [1, 2, 3, 4])
        self.assertEqual(c, 5)

    def test_unpack_into_exprlist_4(self):
        a, b, *c = range(6)
        self.assertEqual(a, 0)
        self.assertEqual(b, 1)
        self.assertEqual(c, [2, 3, 4, 5])

    def test_unpack_into_exprlist_5(self):
        a, b, *c, d = e, *f, g, h = range(6)
        self.assertEqual(a, 0)
        self.assertEqual(b, 1)
        self.assertEqual(c, [2, 3, 4])
        self.assertEqual(d, 5)

        self.assertEqual(e, 0)
        self.assertEqual(f, [1, 2, 3])
        self.assertEqual(g, 4)
        self.assertEqual(h, 5)

    def test_unpack_into_list_1(self):
        [*a] = range(2)
        self.assertEqual(a, [0, 1])

    def test_unpack_into_list_2(self):
        [*a, b] = range(2)
        self.assertEqual(a, [0])
        self.assertEqual(b, 1)

    def test_unpack_into_list_3(self):
        [a, *b, c] = range(5)
        self.assertEqual(a, 0)
        self.assertEqual(b, [1, 2, 3])
        self.assertEqual(c, 4)

    def test_unpack_into_for_target_1(self):
        index = 0
        for a, *b in enumerate(range(3)):
            self.assertEqual(a, index)
            self.assertEqual(b, [index])
            index = index + 1

    def test_unpack_into_for_target_2(self):
        index = 0
        for *a, b in enumerate(range(3)):
            self.assertEqual(b, index)
            self.assertEqual(a, [index])
            index = index + 1

    def test_unpack_into_for_target_3(self):
        index = 0
        expected_a = [1, 4]
        expected_b = [[2], [8, 3]]
        expected_c = [3, 1]

        for a, *b, c in [(1, 2, 3), (4, 8, 3, 1)]:
            self.assertEqual(a, expected_a[index])
            self.assertEqual(b, expected_b[index])
            self.assertEqual(c, expected_c[index])
            index = index + 1

    def test_too_many_starred_assignments(self):
        msg = "multiple starred expressions in assignment" if sys.version_info >= (3,9) else "two starred expressions in assignment"
        self.assertRaisesSyntaxError("*x, *k = range(5)", msg)
        self.assertRaisesSyntaxError("*x, *k, *r = range(5)", msg)
        self.assertRaisesSyntaxError("v, *x, n, *k = range(5)", msg)
        self.assertRaisesSyntaxError("h, t, *g, s, *x, m, *k = range(5)", msg)

        self.assertRaisesSyntaxError("[*x, *k] = range(5)", msg)
        self.assertRaisesSyntaxError("[*x, *k, *r] = range(5)", msg)
        self.assertRaisesSyntaxError("[v, *x, n, *k] = range(5)", msg)
        self.assertRaisesSyntaxError("[h, t, *g, s, *x, m, *k] = range(5)", msg)

    def test_assignment_to_unassignable_targets(self):
        literal_msg = "cannot assign to literal" if sys.version_info >= (3,8) else "can't assign to literal"
        operator_msg = "cannot assign to operator" if sys.version_info >= (3,8) else "can't assign to operator"
        self.assertRaisesSyntaxError('[x, y, "a", z] = range(4)', literal_msg)
        self.assertRaisesSyntaxError('[x, y, a + 1, z] = range(4)', operator_msg)

        self.assertRaisesSyntaxError('(x, y, "a", z) = range(4)', literal_msg)
        self.assertRaisesSyntaxError('(x, y, a + 1, z) = range(4)', operator_msg)

        self.assertRaisesSyntaxError('x, y, "a", z = range(4)', literal_msg)
        self.assertRaisesSyntaxError('x, y, a + 1, z = range(4)', operator_msg)

    def test_too_many_expressions_in_star_unpack(self):
        body = ", ".join("a%d" % i for i in range(1<<8)) + ", *rest = range(1<<8 + 1)"
        self.assertRaisesSyntaxError(body, "too many expressions in star-unpacking assignment")

        body = "[" + ", ".join("a%d" % i for i in range(1<<8)) + ", *rest] = range(1<<8 + 1)"
        self.assertRaisesSyntaxError(body, "too many expressions in star-unpacking assignment")

    def test_assign_to_empty(self):
        () = [] # new in 3.6
        [] = ()

    def test_assign_trailing_comma_list_to_list(self):
        [a, *b,] = [1, 2, 3]
        self.assertEqual(a, 1)
        self.assertEqual(b, [2, 3])

        [c, *d] = [1, 2, 3,]
        self.assertEqual(c, 1)
        self.assertEqual(d, [2, 3])

        [e, *f,] = [1, 2, 3,]
        self.assertEqual(e, 1)
        self.assertEqual(f, [2, 3])

    def test_assign_trailing_comma_list_to_tuple(self):
        (a, *b,) = [1, 2, 3]
        self.assertEqual(a, 1)
        self.assertEqual(b, [2, 3])

        (c, *d) = [1, 2, 3,]
        self.assertEqual(c, 1)
        self.assertEqual(d, [2, 3])

        (e, *f,) = [1, 2, 3,]
        self.assertEqual(e, 1)
        self.assertEqual(f, [2, 3])

    def test_assign_trailing_comma_tuple_to_list(self):
        [a, *b,] = (1, 2, 3)
        self.assertEqual(a, 1)
        self.assertEqual(b, [2, 3])

        [c, *d] = (1, 2, 3,)
        self.assertEqual(c, 1)
        self.assertEqual(d, [2, 3])

        [e, *f,] = (1, 2, 3,)
        self.assertEqual(e, 1)
        self.assertEqual(f, [2, 3])

    def test_assign_trailing_comma_tuple_to_tuple(self):
        (a, *b,) = (1, 2, 3)
        self.assertEqual(a, 1)
        self.assertEqual(b, [2, 3])

        (c, *d) = (1, 2, 3,)
        self.assertEqual(c, 1)
        self.assertEqual(d, [2, 3])

        (e, *f,) = (1, 2, 3,)
        self.assertEqual(e, 1)
        self.assertEqual(f, [2, 3])

    def test_assign_multiple_trailing_commas_fails(self):
        self.assertRaisesSyntaxError('[a, *b,,] = [1, 2, 3]', "invalid syntax")
        self.assertRaisesSyntaxError('(a, *b,,) = [1, 2, 3]', "invalid syntax")
        self.assertRaisesSyntaxError('[a, *b] = [1, 2, 3,,]', "invalid syntax")
        self.assertRaisesSyntaxError('(a, *b) = [1, 2, 3,,]', "invalid syntax")

        self.assertRaisesSyntaxError('[a, *b,,] = (1, 2, 3)', "invalid syntax")
        self.assertRaisesSyntaxError('(a, *b,,) = (1, 2, 3)', "invalid syntax")
        self.assertRaisesSyntaxError('[a, *b] = (1, 2, 3,,)', "invalid syntax")
        self.assertRaisesSyntaxError('(a, *b) = (1, 2, 3,,)', "invalid syntax")

    def test_delete_star_fails(self):
        if sys.version_info >= (3,9):
            msg = "cannot delete starred"
        elif sys.implementation.name == "ironpython" or sys.version_info >= (3,5):
            msg = "can't use starred expression here"
        else:
            msg = "can use starred expression only as assignment target"
        self.assertRaisesSyntaxError('del *a', msg)
        self.assertRaisesSyntaxError('del *a, b', msg)
        self.assertRaisesSyntaxError('del b, *a', msg)

    def test_ipy3_gh841(self):
        "https://github.com/IronLanguages/ironpython3/issues/841"
        x = [1, 2, 3]
        x.pop()
        a, *b = x
        self.assertEqual(a, 1)
        self.assertEqual(b, [2])

    @unittest.skipUnless(sys.implementation.name == "ironpython" or sys.version_info >= (3,5), "new syntax in 3.5")
    def test_unpack_dict(self):
        # TODO: remove eval once our baseline is >= 3.5
        self.assertEqual(eval("{'x': 1, **{'y': 2}}"), {'x': 1, 'y': 2})
        self.assertEqual(eval("{'x': 1, **{'x': 2}}"), {'x': 2})
        self.assertEqual(eval("{**{'x': 2}, 'x': 1}"), {'x': 1})

        # TODO: remove exec once our baseline is >= 3.5
        with self.assertRaises(TypeError):
            exec("{**[]}")

    @unittest.skipUnless(sys.implementation.name == "ironpython" or sys.version_info >= (3,5), "new syntax in 3.5")
    def test_unpack_sequence(self):
        # TODO: remove eval once our baseline is >= 3.5
        self.assertEqual(eval("(*range(4), 4)"), (0,1,2,3,4))
        self.assertEqual(eval("[*range(4), 4]"), [0,1,2,3,4])
        self.assertEqual(eval("{*range(4), 4}"), {0,1,2,3,4})

        # TODO: remove exec once our baseline is >= 3.5
        with self.assertRaises(TypeError):
            exec("(*1,)")

        with self.assertRaises(TypeError):
            exec("[*1]")

        with self.assertRaises(TypeError):
            exec("{*1}")

def test_main():
    test.support.run_unittest(UnpackTest)

if __name__ == "__main__":
    test_main()
