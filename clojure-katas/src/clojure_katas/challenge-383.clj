(ns clojure-katas.challenge-383
  (:require
   [clojure.tools.logging :as log]
   [clojure.string :as s]))

;; challenge
(defn same_necklace [str-a str-b]
  (if (= (count str-a) (count str-b))
      (let [str-b-double (str str-b str-b)]
        (s/includes? str-b-double str-a))
      false))

;; bonus #1
(defn transpose-and-check-if-same [input-str modified-str times]
  (if-not (zero? times)
    (let [head (first modified-str)
          rest (next modified-str)
          new-modified-str (str (s/join rest) head)
          new-times (- times 1)]
      (if (= input-str modified-str)
        (+ 1 (transpose-and-check-if-same input-str new-modified-str new-times))
        (+ 0 (transpose-and-check-if-same input-str new-modified-str new-times))))
    0))

(defn repeats [input-str]
  (let [length (count input-str)
        head (first input-str)
        rest (next input-str)]
    (transpose-and-check-if-same input-str (str (s/join rest) head) length)))
