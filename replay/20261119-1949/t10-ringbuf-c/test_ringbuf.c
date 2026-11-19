#include <assert.h>

#include "ringbuf.h"

static void test_fill_and_overflow(void)
{
    int s[3];
    int v = 0;
    struct ringbuf r;
    rb_init(&r, s, 3);
    assert(rb_len(&r) == 0);
    assert(rb_push(&r, 1) == 0);
    assert(rb_push(&r, 2) == 0);
    assert(rb_push(&r, 3) == 0);
    assert(rb_len(&r) == 3);
    assert(rb_push(&r, 4) == -1);
    assert(rb_len(&r) == 3);
    assert(rb_pop(&r, &v) == 0 && v == 1);
    assert(rb_pop(&r, &v) == 0 && v == 2);
    assert(rb_pop(&r, &v) == 0 && v == 3);
    assert(rb_len(&r) == 0);
}

static void test_empty_pop(void)
{
    int s[2];
    int v = 42;
    struct ringbuf r;
    rb_init(&r, s, 2);
    assert(rb_pop(&r, &v) == -1);
    assert(v == 42);
    assert(rb_len(&r) == 0);
}

static void test_wrap_around(void)
{
    int s[3];
    int v = 0;
    struct ringbuf r;
    rb_init(&r, s, 3);
    assert(rb_push(&r, 1) == 0);
    assert(rb_push(&r, 2) == 0);
    assert(rb_push(&r, 3) == 0);
    assert(rb_pop(&r, &v) == 0 && v == 1);
    assert(rb_push(&r, 4) == 0);
    assert(rb_pop(&r, &v) == 0 && v == 2);
    assert(rb_pop(&r, &v) == 0 && v == 3);
    assert(rb_pop(&r, &v) == 0 && v == 4);
    assert(rb_pop(&r, &v) == -1);
    assert(rb_len(&r) == 0);
}

int main(void)
{
    test_fill_and_overflow();
    test_empty_pop();
    test_wrap_around();
    return 0;
}
