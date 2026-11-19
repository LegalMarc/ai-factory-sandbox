#include <assert.h>
#include "ringbuf.h"

int main(void) {
    int storage[3];
    int v = 0;
    struct ringbuf rb;

    rb_init(&rb, storage, 3);

    /* empty pop */
    assert(rb_pop(&rb, &v) == -1);
    assert(rb_len(&rb) == 0);

    /* fill and overflow */
    assert(rb_push(&rb, 1) == 0);
    assert(rb_push(&rb, 2) == 0);
    assert(rb_push(&rb, 3) == 0);
    assert(rb_push(&rb, 4) == -1);
    assert(rb_len(&rb) == 3);

    /* wrap around */
    assert(rb_pop(&rb, &v) == 0 && v == 1);
    assert(rb_push(&rb, 5) == 0);
    assert(rb_pop(&rb, &v) == 0 && v == 2);
    assert(rb_pop(&rb, &v) == 0 && v == 3);
    assert(rb_pop(&rb, &v) == 0 && v == 5);
    assert(rb_pop(&rb, &v) == -1);
    assert(rb_len(&rb) == 0);

    return 0;
}
